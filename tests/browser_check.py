"""Check the actual publication artifact over HTTP under /portfolio/."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory
from threading import Thread
from urllib.parse import unquote, urlsplit
import shutil
import subprocess
import sys

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def check_files(site):
    pages = sorted(site.rglob('*.html'))
    for file in pages:
        doc = BeautifulSoup(file.read_text(), 'html.parser')
        assert doc.html.get('lang'), file
        assert len(doc.select('h1')) == 1, file
        assert doc.title and doc.title.get_text(strip=True), file
        ids = [node['id'] for node in doc.select('[id]')]
        assert len(ids) == len(set(ids)), f'Duplicate IDs: {file}'
        for node in doc.select('[href], [src]'):
            link = node.get('href', node.get('src', ''))
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (file.parent / unquote(parsed.path)).resolve() if parsed.path else file
            assert target.is_relative_to(site.resolve()), (file, link)
            assert target.is_file(), (file, link)
            if parsed.fragment:
                target_doc = BeautifulSoup(target.read_text(), 'html.parser')
                assert target_doc.find(id=unquote(parsed.fragment)), (file, link)
    assert not (site / 'docs').exists()
    assert not (site / '.git').exists()
    assert not (site / 'README.md').exists()
    assert not (site / 'tests').exists()
    assert not (site / 'private').exists()
    return pages


def check_browser(site, base, pages):
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={'width': 1440, 'height': 1000}, reduced_motion='reduce')
        errors = []
        failed = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('requestfailed', lambda request: failed.append(request.url))
        page.goto(base)
        assert page.locator('.card:visible').count() == 8
        for category, count in [('detection', 3), ('cloud', 3), ('devsecops', 2), ('all', 8)]:
            button = page.locator(f'button[data-filter="{category}"]')
            button.click()
            assert button.get_attribute('aria-pressed') == 'true'
            assert page.locator('.card:visible').count() == count
            assert str(count) in page.locator('.filter-status').inner_text()
        page.locator('button[data-filter="cloud"]').click()
        page.locator('#kompetens a[href="#soc"]').click()
        assert page.locator('#soc').is_visible()
        assert page.locator('.card:visible').count() == 8
        for width in [320, 390, 768, 1440]:
            page.set_viewport_size({'width': width, 'height': 900})
            for file in pages:
                response = page.goto(base + file.relative_to(site).as_posix())
                assert response.status == 200, file
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), (width, file)
                assert page.locator('h1').count() == 1
                assert page.locator('img').evaluate_all('(images) => images.every(i => i.complete && i.naturalWidth > 0)'), file
        page.goto(base)
        page.keyboard.press('Tab')
        assert page.locator('.skip').evaluate('(e) => e === document.activeElement')
        page.keyboard.press('Enter')
        assert page.evaluate('location.hash') == '#main'
        page.locator('button[data-filter="cloud"]').click()
        page.emulate_media(media='print')
        assert page.locator('.card:visible').count() == 8
        page.emulate_media(media='screen')
        assert page.locator('a[href="mailto:j.nguyen92@hotmail.com"]').count() == 1
        for language in ['sv', 'en']:
            link = page.locator(f'#kontakt a[href="assets/jonny-nguyen-cv-{language}.pdf"]')
            with page.expect_download() as download:
                link.click()
            data = Path(download.value.path()).read_bytes()
            assert data.startswith(b'%PDF-'), language
        for path in ['README.md', 'docs/content-sources.md', '.git/config', 'private/example.pdf']:
            assert page.request.get(base + path).status == 404, path
        nojs = browser.new_context(java_script_enabled=False)
        fallback = nojs.new_page()
        fallback.goto(base)
        assert fallback.locator('.card:visible').count() == 8
        assert not fallback.locator('.filters').is_visible()
        fallback.locator('#ml h3 a').click()
        assert fallback.locator('h1').count() == 1
        assert not errors, errors
        assert not failed, failed
        browser.close()


def main():
    subprocess.run([sys.executable, str(ROOT / 'scripts/build_site.py')], check=True)
    with TemporaryDirectory() as directory:
        site = Path(directory) / 'portfolio'
        shutil.copytree(ROOT / '_site', site)
        pages = check_files(site)
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=directory))
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            check_browser(site, f'http://127.0.0.1:{server.server_port}/portfolio/', pages)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
    print(f'PASS: {len(pages)} HTML pages over HTTP at four widths; local links, filters, keyboard, downloads, print, no-JS and excluded private files.')


if __name__ == '__main__':
    main()

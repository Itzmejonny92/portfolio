"""Prepare only reviewed website files for static hosting; never publish the repo root."""
import argparse
from html import escape
from pathlib import Path
import shutil
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '_site'
ASSETS = [
    'jonny-nguyen.png', 'jonny-nguyen-cv-sv.pdf', 'jonny-nguyen-cv-en.pdf',
    'jonny-nguyen-cv-sv.html', 'jonny-nguyen-cv-en.html',
]


def build(site_url):
    parts = urlsplit(site_url)
    if parts.scheme != 'https' or not parts.netloc or parts.query or parts.fragment:
        raise ValueError('Use an absolute HTTPS site URL without query or fragment.')
    site_url = site_url.rstrip('/') + '/'
    if OUTPUT.is_symlink():
        raise ValueError('_site must not be a symlink.')
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    files = [ROOT / f for f in ['index.html', 'styles.css', 'script.js', 'favicon.svg', '.nojekyll']]
    files += sorted((ROOT / 'projekt').glob('*.html'))
    files += [ROOT / 'assets' / name for name in ASSETS]
    pages = []
    for source in files:
        if source.is_symlink() or not source.is_file():
            raise ValueError(f'Expected a regular website file: {source}')
        relative = source.relative_to(ROOT)
        target = OUTPUT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        if source.suffix == '.html':
            url = site_url + ('' if relative.as_posix() == 'index.html' else relative.as_posix())
            metadata = f'<link rel="canonical" href="{escape(url, quote=True)}">\n'
            metadata += f'<meta property="og:url" content="{escape(url, quote=True)}">\n'
            target.write_text(target.read_text().replace('</head>', metadata + '</head>'))
            pages.append(url)
    # Absolute site URL also works for an unknown, deeply nested missing path.
    (OUTPUT / '404.html').write_text(f'''<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Sidan hittades inte | Jonny Nguyen</title><style>body{{margin:0;background:#f7f7f0;color:#18332e;font:18px/1.6 Arial,sans-serif}}main{{max-width:760px;padding:60px 24px;margin:auto}}h1{{font-size:42px;line-height:1.1}}a{{color:inherit;text-underline-offset:5px}}a:focus-visible{{outline:3px solid #698637;outline-offset:5px}}</style></head><body><main><section><p class="eyebrow">404 / SIDAN HITTADES INTE</p><h1>Vi hittar tillbaka.</h1><p>Länken kan vara gammal eller adressen felstavad.</p><a class="button" href="{escape(site_url)}">Till Jonny Nguyens portfolio →</a></section></main></body></html>''')
    entries = ''.join(f'<url><loc>{escape(url)}</loc></url>' for url in pages)
    (OUTPUT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{entries}</urlset>')
    print(f'Prepared {len(files) + 2} public files in {OUTPUT}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-url', default='https://itzmejonny92.github.io/portfolio/')
    build(parser.parse_args().site_url)

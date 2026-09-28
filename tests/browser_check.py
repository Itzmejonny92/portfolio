from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1];base=root.as_uri()
with sync_playwright() as pw:
 browser=pw.chromium.launch()
 page=browser.new_page(viewport={'width':1440,'height':1000},reduced_motion='reduce');errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(base+'/index.html')
 assert page.locator('.card:visible').count()==8
 for cat,count in [('detection',3),('cloud',3),('devsecops',2),('all',8)]:
  page.locator(f'button[data-filter="{cat}"]').click();assert page.locator('.card:visible').count()==count
 page.locator('button[data-filter="cloud"]').click();page.locator('#kompetens a[href="#soc"]').click();assert page.locator('#soc').is_visible();assert page.locator('.card:visible').count()==8
 for width in [320,390,768,1440]:
  page.set_viewport_size({'width':width,'height':900})
  for file in [root/'index.html',*sorted((root/'projekt').glob('*.html'))]:
   page.goto(file.as_uri());assert page.locator('h1').count()==1
   assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),(width,file.name)
   for link in page.locator('a[href]').all():
    href=link.get_attribute('href')
    if href.startswith('https:'):continue
    path,_,anchor=href.partition('#');target=(file.parent/path).resolve() if path else file
    assert target.exists(),(file,href)
 page.goto(base+'/index.html');page.keyboard.press('Tab');assert page.locator('.skip').evaluate('(e)=>e===document.activeElement');page.keyboard.press('Enter');assert page.evaluate('location.hash')=='#main'
 page.locator('button[data-filter="cloud"]').click();page.emulate_media(media='print');assert page.locator('.card:visible').count()==8
 nojs=browser.new_context(java_script_enabled=False);fallback=nojs.new_page();fallback.goto(base+'/index.html');assert fallback.locator('.card:visible').count()==8;assert not fallback.locator('.filters').is_visible()
 assert not errors,errors
 browser.close();print('PASS: 9 pages at 4 widths, filters, hidden anchor navigation, keyboard skip link, print, no-JavaScript fallback, no browser errors.')

# Publiceringsgranskning · 2026-09-29

## Bedömning

Webbplatsen är publicerad och verifierad på **https://itzmejonny92.github.io/portfolio/**. Jonny godkände publiceringen 2026-09-29. Repot är nu publikt och GitHub Pages använder det separat byggda webbpaketet. Webbplatsen kräver ingen GitHub-inloggning.

## Granskat och åtgärdat

- Genomläst startsida, alla åtta projektbeskrivningar, CV-underlag i repot och projektdokumentation. Rättat ett grammatiskt fel och missvisande dubbelnumrering på projektsidor.
- Rättat gammal dokumentation som fortfarande sade att CV-uppgifter saknades.
- Arbetslivserfarenheten beskrivs som produktionsledning. Utbildningen är pågående. Teamarbete, egna bidrag och historiska labbresultat är avgränsade.
- Rättat sidregioner för hjälpmedel på startsidan och CV-källorna; projektlänkar har tydligare tillgängliga namn.
- Lagt till separat publiceringspaket, kanoniska länkar, sitemap och 404-sida.
- Lagt till automatiska kontroller och manuell Pages-publicering. Inga deploysteg körs vid vanlig push. Actions är låsta till aktuella commit-id:n och körmiljön till Ubuntu 24.04.

## Kontrollresultat

| Kontroll | Resultat |
| --- | --- |
| HTML och interna länkar | Alla lokala mål, resurser och ankare finns; unika id:n |
| Webbserver och undermapp | Paketet testat via HTTP under `/portfolio/` |
| Responsivitet | 12 HTML-sidor vid 320, 390, 768 och 1440 px; ingen horisontell överbredd |
| Funktion | Projektfilter, länkar till dolda kort, hopplänk, utskrift och visning utan JavaScript fungerar |
| CV | Svenska och engelska PDF:er kan laddas ner; en sida vardera med klickbara kontaktlänkar |
| Tillgänglighet | axe-core 4.10.3: inga rapporterade fynd efter rättningar på startsida, åtta projekt och två CV-källor, med WCAG A/AA och best-practice-regler |
| Externa länkar | Nio unika GitHub-länkar ger HTTP 200 utan inloggning |
| LinkedIn | HTTP 999 från automatiserad kontroll; behöver manuell kontroll, inte klassad som trasig |
| Nyckelmönster | Inga träffar på granskade vanliga token-/privatnyckelformat i 49 historiska Git-blobbar före denna ändring |
| Personuppgifter | Avsedda kontaktuppgifter, ort och porträtt ingår; bostadsadress och telefonnummer saknas i PDF-versionerna |
| Webbpaket | Cirka 0,35 MB; dokumentation, tester, `.git` och privata arbetsfiler utesluts |

## Vad kontrollerna inte bevisar

Automatiska tillgänglighetstester ersätter inte manuell skärmläsartestning. Mönstersökning efter nycklar är inte en garanti mot alla hemligheter. Alla tidigare granskade kursprojekt har inte genomgått en ny kodrevision. Webbplatsen har testats i Chromium, inte i varje mobilwebbläsare. HTTPS och anpassad 404-hantering har verifierats efter publicering. Cachebeteende över längre tid har inte särskilt testats.

## Publicerat och verifierat

- **Livelänk:** https://itzmejonny92.github.io/portfolio/
- **Publicerad webbplatsversion:** `6014873` (vitt och rött tema).
- **Deployment:** [36589962633](https://github.com/Itzmejonny92/portfolio/actions/runs/36589962633), både kontroll och deployment lyckades.
- Alla 20 publicerade filer gav HTTP 200 och matchade lokalt granskat paket byte för byte.
- Påhittad djup URL, `docs/content-sources.md` och `.git/config` gav HTTP 404 med den anpassade felsidan.
- Mobilnavigation, projektfilter, porträtt och kontakt kontrollerades i en ny Chromium-session utan inloggning.
- Båda PDF-filerna är tillgängliga över HTTPS.

Hela repot, dess dokumentation och historik är nu offentliga. Själva Pages-webbplatsen innehåller enbart filerna i publiceringspaketet. Webbplatsen visar namn, porträtt, Helsingborg, e-post, LinkedIn, GitHub, arbetslivsbakgrund, utbildningsperiod och två CV-filer.

Inga formulär eller egna spårningsskript används. GitHub Pages kan logga besökares IP-adresser för säkerhetsändamål enligt [GitHubs dokumentation](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

LinkedIn-länken är tillhandahållen av Jonny men blockerade den automatiska kontrollen. Tillgänglighet för LIA/anställning kan kompletteras senare.

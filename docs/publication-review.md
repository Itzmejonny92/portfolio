# Publiceringsgranskning · 2026-09-29

## Bedömning

Webbplatsen är tekniskt förberedd för publicering, med rättningar och verifiering enligt nedan. Den är ännu inte live. GitHub-repot är privat och saknar aktiverad Pages-webbplats. Slutlig synlighet och publicering behöver beslutas innan en arbetsgivarlänk kan verifieras.

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

Automatiska tillgänglighetstester ersätter inte manuell skärmläsartestning. Mönstersökning efter nycklar är inte en garanti mot alla hemligheter. Alla tidigare granskade kursprojekt har inte genomgått en ny kodrevision. Webbplatsen har testats i Chromium, inte i varje mobilwebbläsare. Slutlig HTTPS-, cache- och 404-hantering på GitHub Pages kan verifieras först efter aktivering.

## Beslut inför publicering

Förslaget är GitHub Pages på `https://itzmejonny92.github.io/portfolio/`. Om hela repot görs publikt blir även dokumentation och historik offentliga, inklusive namn på privata projekt i inventeringen. Ett alternativ är att behålla källrepot privat och använda hosting som stöder det. Kontots planinformation gick inte att avgöra genom API-svaret.

Den aktuella webbplatsen visar namn, porträtt, Helsingborg, e-post, LinkedIn, GitHub, arbetslivsbakgrund, utbildningsperiod och två CV-filer. Inga formulär, spårningsskript eller externa resurser laddas vid sidbesök.

När publicering har genomförts ska den faktiska livelänken verifieras utloggat och läggas i README. Tillgänglighet för LIA/anställning kan kompletteras senare och blockerar inte den nuvarande presentationen.

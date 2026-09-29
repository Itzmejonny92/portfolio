# Verifiering av utvecklad portfolio

2026-09-28:

- Samtliga nio HTML-sidor kontrollerade i Chromium vid 320, 390, 768 och 1440 pixlars bredd.
- Ingen horisontell överbredd vid dessa storlekar.
- Filtren visar 8, 3, 3 respektive 2 projekt.
- Kompetenslänkar återvisar kort som dolts av ett filter.
- Hopplänken kan nås och användas med tangentbord.
- Utskriftsläget visar alla projekt även efter filtrering.
- Alla projekt och fördjupningssidor fungerar utan JavaScript.
- Inga JavaScript-fel i webbläsaren under testen.
- Lokala filer och ankarlänkar mellan samtliga sidor kontrollerade.
- Desktop- och mobilskärmbilder granskade visuellt.

Automatiska kontroller och skärmbilder kompletterar, men ersätter inte, en fullständig tillgänglighetsgranskning med skärmläsare. Externa länkar har behållits från det tidigare granskade GitHub-underlaget; detta test verifierar lokala länkar.

## Efter komplettering med CV-underlag

Alla nio portfoliosidor klarade åter webbläsartesterna på fyra skärmbredder. CV-filerna på svenska och engelska är en sida vardera; e-post finns med och bostadsadress samt telefonnummer har utelämnats. Porträtt- och CV-länkarna pekar på lokala filer. LinkedIn-länken är tillhandahållen av Jonny; profilinnehållet kunde inte hämtas.

## Publiceringsgranskning 2026-09-29

Den utökade verifieringen av webbpaketet via HTTP, tillgänglighet, externa länkar och publiceringsförberedelser finns i [publiceringsgranskningen](publication-review.md). Den ersätter tidigare begränsning att endast lokala filer testades.

## Vitt och rött tema · 2026-09-29

Webbplats, favicon, 404-sida och båda CV-versionerna har fått ett vitt och rött tema. HTTP-testerna passerar på fyra skärmbredder. Axe-kontrollen av startsida, åtta projektsidor och två CV-källor rapporterar inga fynd efter färgbytet. Desktoplayouten är visuellt granskad.

# Underhåll och publicering

## Arbeta lokalt

Kör kommandona från portfolio-repots rot, inte från teamets `company-website`.

```sh
git status --short --branch
git pull --ff-only
python3 -m http.server 8000 --bind 127.0.0.1
```

Öppna http://localhost:8000. Stoppa servern med Ctrl+C. Om Git rapporterar lokala ändringar eller divergerade brancher, granska dem innan du fortsätter; använd inte reset för att synka bort eget arbete.

## Var ändras innehållet?

| Ändring | Filer |
| --- | --- |
| Presentation och kontakt | `index.html`, avsnitten `om` och `kontakt`; även README |
| Projektets korta sammanfattning | `index.html` |
| Uppgift, bidrag, resultat och källor | Motsvarande sida i `projekt/` |
| Utseende och mobilvy | `styles.css` |
| Projektfilter | `script.js` och kortens `data-category` |
| Nytt projekt eller nytt filter | Uppdatera även antal och förväntningar i `tests/browser_check.py` |
| Källor och avgränsningar | `docs/content-sources.md` |

Navigation och sidfot finns i varje HTML-fil. Ändringar som gäller hela webbplatsen behöver därför göras på alla nio sidor. HTML-sidorna redigeras direkt utan sidgenerator. Inför publicering paketerar `scripts/build_site.py` bara avsedda filer och lägger till publiceringsmetadata.

## Kontakt, CV och privata arbetsfiler

Kontaktsektionen innehåller e-post, LinkedIn och GitHub samt ort. Uppdatera både `index.html` och README när uppgifterna ändras.

CV finns som `assets/jonny-nguyen-cv-sv.pdf` och `assets/jonny-nguyen-cv-en.pdf`. Motsvarande HTML-filer i samma mapp är redigerbara källor. Öppna dem i en webbläsare och skriv ut till PDF med A4, utan webbläsarens sidhuvud/sidfot, efter innehållsändringar. Kontrollera att slutresultatet fortfarande ryms och att länkar fungerar. Porträttet ligger i `assets/jonny-nguyen.png`.

CV-versionerna för webben utelämnar bostadsadress och telefonnummer. Originalunderlaget ligger utanför repot. Privata utkast kan förvaras i den ignorerade mappen `private/`. En gitignore-regel tar inte bort redan versionshanterade filer. Ladda bara upp avsedda webbplatsfiler vid publicering.

## Kontroll före push

```sh
python tests/browser_check.py
git diff --check
git diff --stat
git status --short
```

Testmiljön installeras enligt README. Läs också igenom det ändrade innehållet och kontrollera att källorna stöder nya påståenden. För kontaktlänkar: kontrollera adress och länkdestination, inte bara den synliga texten.

## Publicering på GitHub Pages

Status 2026-09-29: repot är privat och Pages är inte aktiverat. Publicering är förberedd men inte utförd.

1. Bestäm om hela repot ska vara publikt eller om bara webbplatsen ska vara publik. Ett publikt repo gör även dokumentation och Git-historik tillgängliga. Pages från privat repo kräver en stödjande GitHub-plan; kontots plan kunde inte fastställas via API.
2. När synligheten är beslutad: välj **Settings → Pages → Source: GitHub Actions**.
3. Kör workflowen **Portfolio checks and manual publishing** manuellt från `main`. Vanliga pushar och PR:er kör enbart kontroller.
4. Testjobbet bygger `_site/`, kontrollerar det via HTTP och laddar upp enbart det paketet. Deployjobbet körs bara om kontrollerna lyckas. Inga långlivade deploynycklar används.
5. Kontrollera den faktiska Pages-adressen i en utloggad webbläsare: startsida, projektsidor, porträtt, båda CV-filerna och en påhittad adress för 404-sidan. Kontrollera även LinkedIn manuellt.
6. När sidan fungerar: lägg den bekräftade livelänken överst i README och i repots About-fält. Använd den länken i ansökningar.

Standardadressen i bygget är `https://itzmejonny92.github.io/portfolio/`. Byter du värd, domän eller repo-namn behöver standardvärdet för `--site-url` i `scripts/build_site.py` uppdateras, eftersom CI-testet anropar bygget med dess standardvärde. Den styr sitemap, kanoniska länkar och 404-sidans länk till startsidan.

Publicera alltid `_site/`, inte hela repots rot. Paketet bygger på en lista av webbplatsfiler och innehåller inga `docs/`, testverktyg, README eller Git-metadata. De redigerbara CV-källorna ingår avsiktligt och innehåller samma avsedda publika uppgifter som PDF-versionerna. Även en PDF-länk kan hittas av sökmotorer.

Vid fel efter en publicering: återställ ändringen med en ny commit, kör kontrollerna och publicera den fungerande versionen manuellt. Git-historik behöver inte skrivas om.

Referens: [GitHubs information om Pages och planstöd](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

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

Navigation och sidfot finns i varje HTML-fil. Ändringar som gäller hela webbplatsen behöver därför göras på alla nio sidor. Ingen generator eller byggprocess används.

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

## Publicering

Webbplatsen är statisk och kan serveras från repots rot. Den fungerar även under en undermapp eftersom lokala länkar är relativa. `.nojekyll` markerar att ingen Jekyll-bearbetning behövs på GitHub Pages.

Ingen publicering eller ändring av repots synlighet ingår i den lokala utvecklingen. När publiceringsalternativ och synlighet har valts, använd GitHubs Pages-inställningar eller en annan statisk webbserver. Lägg den verkliga webbplatsadressen i README först när den är aktiv. Ladda inte upp privata arbetsfiler, testmiljöer eller Git-metadata som webbmaterial.

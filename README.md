# Jonny Nguyen · Portfolio

Cybersäkerhet, SOC/SIEM, OT-säkerhet, AI-integration och säker molninfrastruktur. Jag studerar på Chas Academy, ITSX25, och samlar här praktiska kursprojekt, dokumenterade resultat och lärdomar.

[GitHub-profil](https://github.com/Itzmejonny92) · [Portfolio-repo](https://github.com/Itzmejonny92/portfolio)

## Om mig

Jag är Jonny Nguyen, bosatt i Helsingborg, och studerar till IT- och cybersäkerhetstekniker (YH) på Chas Academy, ITSX25, september 2025–juli 2027. Min bakgrund är produktionsledare på KLS Ugglarps AB (2015–2026), med personalansvar, planering, säkerhetsrutiner, riskbedömning och kvalitetssäkring. Jag är intresserad av SOC, Security Engineering och detection engineering. I projekten arbetar jag bland annat med integration, metodisk felsökning och dokumentation som gör tekniska beslut lättare att följa.

## Kontakt

- **GitHub:** [Itzmejonny92](https://github.com/Itzmejonny92)
- **E-post:** [j.nguyen92@hotmail.com](mailto:j.nguyen92@hotmail.com)
- **LinkedIn:** [Jonny Nguyen](https://www.linkedin.com/in/jonny-nguyen-770463383/)
- **Ort:** Helsingborg, Sverige
- **CV:** [Svenska (PDF)](assets/jonny-nguyen-cv-sv.pdf) · [English (PDF)](assets/jonny-nguyen-cv-en.pdf)

## Projekt att börja med

| Projekt | Vad det visar | Underlag |
| --- | --- | --- |
| Wazuh / SIEM | Centraliserad säkerhetsövervakning och nätverksanalys. Individuell labb. | [Publik reflektion](https://github.com/Itzmejonny92/AIS-slutreflektion) |
| OT/ICS | Segmentering, Suricata och incidentrespons i simulerad miljö. Individuell labb. | [Publik reflektion](https://github.com/Itzmejonny92/AIS-slutreflektion) |
| ML Network Anomaly Detector | Min roll: SIEM/SOAR-integration, testning, dokumentation och demo. Teamprojekt. | [Publik beskrivning av min roll](https://github.com/Itzmejonny92/AIS-slutreflektion) |
| Team 2 Infrastruktur | WIF, IAM, Terraform och nätverksfelsökning. Teamprojekt. | [Mina arbetsanteckningar](https://github.com/itsx25-team2/kurs6-team2-infra/tree/main/members/itzmejonny92) |
| M4K Pipeline / GKE | Gemensam pipeline och personlig Kubernetes-labb. | [Min GKE-labb](https://github.com/Itzmejonny92/M4K-Pipeline-main/blob/main/docs/reports/week6-labb-jonny-nguyen.md) |
| Container Security | Härdning, skanning, SBOM och policykontroller. Individuell labb. | [Kod och resultat](https://github.com/Itzmejonny92/lab2-container-security) |
| Terraform för GCP | Infrastruktur som kod, Linux-härdning och backup. Individuell labb. | [Kod och dokumentation](https://github.com/Itzmejonny92/lab1-terraform) |
| Company Website | Applikationshärdning, CI/CD och verifierad leverans. Teamprojekt. | [Mitt dokumenterade bidrag](https://github.com/itsx25-team2/company-website/blob/main/members/itzmejonny92/work_summary_2026-09-28.md) |
| Nätverks-, OT- och AI-säkerhet | Individuell reflektion kring kursens säkerhetsområden. | [Rapport](https://github.com/Itzmejonny92/AIS-slutreflektion) |
| Molnsäkerhet och DevSecOps | SRE, systemresiliens och incidenthantering. | [Slutrapport](https://github.com/Itzmejonny92/slutrapport-jonny-nguyen) |

## Öppna portfolion

Webbplatsen är granskad och förberedd för publicering. Repot är fortfarande privat och GitHub Pages är inte aktiverat. Den planerade adressen är `https://itzmejonny92.github.io/portfolio/`; den ska inte skickas som livelänk förrän publicering och extern kontroll är klara.

Se [publiceringsgranskningen](docs/publication-review.md) för resultat och nästa steg.


Öppna `index.html` direkt i en webbläsare, eller kör från repots rot:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Besök sedan http://localhost:8000. Webbplatsen använder HTML, CSS och ett litet JavaScript för filtrering, utan installation, byggsteg, externa typsnitt eller analysverktyg.

## Struktur

- `index.html` – presentation, filtrerbar projektöversikt, kompetens och profil.
- `projekt/` – åtta fördjupningssidor med uppgift, bidrag, arbetsflöde och lärdomar.
- `script.js` – projektfilter; allt innehåll fungerar även utan JavaScript.
- `styles.css` – responsiv design, tangentbordsfokus och utskriftsvy.
- `favicon.svg` – initialer som webbikon.
- `assets/` – porträtt och CV på svenska och engelska.
- `docs/content-sources.md` – källor och avgränsningar för presentationen.
- `docs/personalization.md` – kontaktuppgifter och CV att komplettera.
- `docs/maintenance.md` – redigering, kontroller och publicering.
- `docs/github-inventory.md` – inventering av GitHub-projekten.
- `docs/verification.md` – genomförda kontroller och deras avgränsningar.
- `tests/browser_check.py` – testar det färdiga webbpaketet via HTTP under `/portfolio/`.
- `scripts/build_site.py` – kopierar endast avsedda webbplatsfiler till `_site/`.
- `.github/workflows/pages.yml` – automatiska kontroller och separat manuell publicering.
- `requirements-dev.txt` – testberoenden; webbplatsen behöver ingen installation.
- `.editorconfig` / `.gitattributes` – gemensamma textformat och radslut.
- `.gitignore` – lokala miljöer, testresultat och privata arbetsfiler.

## Redigera

Ändra presentation och projektöversikt i `index.html`, och längre projektbeskrivningar i `projekt/`. Håll denna README uppdaterad när urvalet ändras. Ange alltid vad som är individuellt arbete respektive teamarbete och länka till underlag. Historiska skanningsresultat ska beskrivas som historiska.

Se [underhållsguiden](docs/maintenance.md) för arbetsflöde och publicering, och [personalisering](docs/personalization.md) för återstående personuppgifter.

## Hela GitHub-underlaget

Se [repoinventeringen](docs/github-inventory.md) för samtliga tillgängliga projekt, urval och avgränsningar. Min publika slutreflektion beskriver intresse för SOC Analyst, Security Engineer och detection engineering; aktuell jobbsökarinriktning behöver fortfarande bekräftas.

## Kontrollera webbplatsen

Webbläsartestet bygger webbpaketet och kontrollerar 12 HTML-sidor: startsida, åtta projekt, två CV-källor och 404-sida. Testet använder HTTP under `/portfolio/` vid 320, 390, 768 och 1440 pixlars bredd. Det kontrollerar även lokala länkar och resurser, ankarlänkar, filter, tangentbordets hopplänk, PDF-nedladdning, utskrift och visning utan JavaScript. Dokumentation, Git-metadata och privata arbetsfiler ska inte gå att hämta från webbpaketet.

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
python -m playwright install --with-deps chromium
python tests/browser_check.py
```

Chromium behöver fungerande systembibliotek. Dessa testberoenden behövs bara för utveckling, inte för att använda eller publicera webbplatsen.

## Design och tillgänglighet

Responsiv layout med lokala typsnitt, tydlig tangentbordsfokus, semantiska sidregioner, reducerad rörelse och utskriftsvy. Filtren visar antal träffar och valt läge för hjälpmedel. Länkar från kompetensdelen visar automatiskt ett projekt även om det dolts av ett filter. Inga externa anrop görs när sidan laddas.

Presentationens texter är ett redaktionellt utkast baserat på projektdokumentationen. Bakgrund, utbildningsperiod och kontaktadress har kompletterats från Jonnys egna CV-filer. Aktuell tillgänglighet för LIA eller anställning återstår att bekräfta.

## Material och återanvändning

Projektbeskrivningarna länkar till originalunderlagen. Teamprojekt och individuella insatser skiljs åt. Ingen generell öppen källkodslicens har valts för detta repo; länkade projekt kan ha egna licenser. Porträtt, CV och andra personliga dokument ska endast läggas till i den version som är avsedd att visas offentligt.

## Publiceringspaket

```sh
python scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory _site
```

`_site/` är genererad och ignoreras av Git. Paketet innehåller inte README, interna anteckningar, tester, Git-historik eller privata arbetsmappar. Bygget lägger till kanoniska sidlänkar, en sitemap och en självständig 404-sida. Annan webbplatsadress anges med `--site-url https://din-domän.example/` för ett enstaka lokalt bygge. För CI-publicering ändras standardvärdet i `scripts/build_site.py`, som testjobbet använder.

Push och pull requests kör kontroller. Publicering kräver en manuell körning av **Portfolio checks and manual publishing** från `main`, efter att Pages och repots synlighet har konfigurerats. Se [underhållsguiden](docs/maintenance.md).

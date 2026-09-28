# Jonny Nguyen · Portfolio

Cybersäkerhet, SOC/SIEM, OT-säkerhet, AI-integration och säker molninfrastruktur. Jag studerar på Chas Academy, ITSX25, och samlar här praktiska kursprojekt, dokumenterade resultat och lärdomar.

[GitHub-profil](https://github.com/Itzmejonny92)

## Börja här

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

## Webbplatsen

Öppna `index.html` direkt i en webbläsare, eller kör från repots rot:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Besök sedan http://localhost:8000. Webbplatsen använder vanlig HTML och CSS, utan installation, byggsteg, externa typsnitt eller analysverktyg.

## Struktur

- `index.html` – presentation, filtrerbar projektöversikt, kompetens och profil.
- `projekt/` – åtta fördjupningssidor med uppgift, bidrag, arbetsflöde och lärdomar.
- `script.js` – projektfilter; allt innehåll fungerar även utan JavaScript.
- `styles.css` – responsiv design, tangentbordsfokus och utskriftsvy.
- `favicon.svg` – initialer som webbikon.
- `docs/content-sources.md` – källor och avgränsningar för presentationen.
- `docs/personalization.md` – uppgifter att komplettera och publiceringsanvisningar.

## Redigera

Ändra presentation och projektöversikt i `index.html`, och längre projektbeskrivningar i `projekt/`. Håll denna README uppdaterad när urvalet ändras. Ange alltid vad som är individuellt arbete respektive teamarbete och länka till underlag. Historiska skanningsresultat ska beskrivas som historiska.

Publiceringsanvisningar och återstående personuppgifter finns i [personalisering](docs/personalization.md).

## Hela GitHub-underlaget

Se [repoinventeringen](docs/github-inventory.md) för samtliga tillgängliga projekt, urval och avgränsningar. Min publika slutreflektion beskriver intresse för SOC Analyst, Security Engineer och detection engineering; aktuell jobbsökarinriktning behöver fortfarande bekräftas.

## Kontrollera webbplatsen

Webbläsartestet kontrollerar alla nio sidor vid 320, 390, 768 och 1440 pixlars bredd, projektfilter, ankarlänkar till dolda kort, tangentbordets hopplänk, utskriftsläge och visning utan JavaScript.

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
python -m playwright install chromium
python tests/browser_check.py
```

Chromium behöver fungerande systembibliotek. Dessa testberoenden behövs bara för utveckling, inte för att använda eller publicera webbplatsen.

## Design och tillgänglighet

Responsiv layout med lokala typsnitt, tydlig tangentbordsfokus, semantiska sidregioner, reducerad rörelse och utskriftsvy. Filtren visar antal träffar och valt läge för hjälpmedel. Länkar från kompetensdelen visar automatiskt ett projekt även om det dolts av ett filter. Inga externa anrop görs när sidan laddas.

Presentationens texter är ett redaktionellt utkast baserat på projektdokumentationen. Aktuell målroll, CV och offentlig kontaktadress återstår att komplettera med Jonny.

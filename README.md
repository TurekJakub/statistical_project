# Statistický projekt

Tento projekt vznikl jako statistický projekt pro předmět Pravděpodobnost a statistika I na MFF UK v akademickém roce 2025/26. Projekt zkoumá vliv aspektů jako je země původu (Kanada x USA), hokejová tradice, či daňová zátěž na výsledky týmu hrajících NHL v sezonách 2005/2006 až 2025/2026. Více informací o práci a jejích výsledcích naleznete v [`reportu`](docs/report.md).

## Spuštění

Pro lokální spuštění všech experimentů vytvořených v rámci projektu nejprve naklonujte tento git repozitář a následně v adresáři projektu spuste následující příkazy.

```bash
python -m venv .venv

source .venv/bin/activate       # Linux/MacOS
.venv\Scripts\activate          # Windows (cmd)
.venv\Scripts\Activate.ps1      # Windows (PowerShell)

pip install -r requirements.txt
```

po dokončění instalace již můžete spustit samotné experimenty pomocí

```bash
python3 -m src.main 

```

V adresáři [`tools`](tools/) zároveň naleznete několik pomocních skriptů pro stažení aktuálních dat, jenž experimenty využívají, nebo jejich vizualizaci.

## Zdrojová data

Pro samotné spuštění experimentů není třeba stahovat žádná další data, tento repozitář obsahuje z důvodu snadné replikovatelnosti výsledků snapshot všech potřebných dat ([`data_import.py`](tools/data_import.py) však lze použít k automatickému stažení aktuálních výsledků playoff z [Hockey-Reference](https://www.hockey-reference.com/)). Zdroj všech použítých externích dat je uveden, jak v přiloženém [`reportu`](docs/report.pdf), tak v [`attribution.md`](resources/attribution.md).

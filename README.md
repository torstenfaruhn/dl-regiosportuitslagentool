# DL regiosport tool (web)

Een kleine Flask‑webapp die je Excel (.xlsx) omzet naar een CUE‑klaar `.txt`‑bestand.
De verwerkingslogica is rechtstreeks overgenomen uit je Colab‑notebook en verpakt
in `converter.py` (functie `excel_to_txt`).

## Lokaal draaien

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py  # http://localhost:8000
```

## Deployen op Render

1. Push deze map naar GitHub.
2. Maak op **Render.com** een *Web Service* aangestuurd door je GitHub‑repo.
3. Render leest `render.yaml`, installeert dependencies en start met `gunicorn`.

## Structuur

- `app.py` – Flask server + routes
- `converter.py` – Excel→TXT omzetting (uit notebook)
- `templates/index.html` – Uploadpagina
- `static/style.css` – Stijlen
- `requirements.txt`, `Procfile`, `render.yaml` – Deploy

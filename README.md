# FIFA World Cup Historical Data Analytics

Historical data exploration in Python using pandas, matplotlib and seaborn.

## Run locally

```bash
cd Football_Analytics_Project
python -m pip install -r requirements.txt
python main.py
```

Expected output: four Matplotlib charts about goal trends, tournament winners,
home-team match results and goal-event patterns. The CSV files are provided in
`Football_Analytics_Project/data/raw/`.

## Repository layout
- `Football_Analytics_Project/main.py`: application entry point.
- `Football_Analytics_Project/src/data_loader.py`: CSV loading.
- `Football_Analytics_Project/src/visualizer.py`: figures.
- `Football_Analytics_Project/requirements.txt`: Python dependencies.
- `Football_Analytics_Project/readme.md`: extended background.
- `.github/workflows/python-checks.yml`: automated smoke check.

This is an exploratory project, not a predictive model. The event parser is
sensitive to dataset formatting; home-team match outcomes are not the same as
host-country causal advantage.

License: MIT for original code; source datasets retain their own terms.

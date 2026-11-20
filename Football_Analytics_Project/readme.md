# FIFA World Cup Historical Data Analytics

Data exploration and visualizations using historical World Cup CSV data.

## Quick start
From repository root:

```bash
cd Football_Analytics_Project
python -m pip install -r requirements.txt
python main.py
```

The Matplotlib windows show goal trends, tournament winners, home-team match outcomes and player event data.

## Actual project structure
- `Football_Analytics_Project/main.py`: entrypoint
- `Football_Analytics_Project/src/data_loader.py`: CSV loading
- `Football_Analytics_Project/src/visualizer.py`: charts
- `Football_Analytics_Project/data/raw/`: historical CSVs
- `Football_Analytics_Project/requirements.txt`: pip dependencies

**Data limitations:** Match home-team status is not identical to being the host nation. Event-string counts are a rough approximation, not validated official goal statistics. The analysis is exploratory, not predictive.

Author: Mohsin Atta

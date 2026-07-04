# ⚽ FIFA World Cup Data Analytics Project

## 📌 Project Overview
This project provides a comprehensive exploratory data analysis (EDA) of the historical FIFA World Cup datasets. The goal is to uncover deep insights regarding tournament trends, team performances, home-field advantages, and player statistics using Python. 

This repository serves as a showcase of practical data manipulation, cleaning, and visualization skills tailored for real-world sports analytics.

## 📂 Dataset Information
The analysis is based on three core datasets sourced from Kaggle:
*   **`WorldCups.csv`**: Contains macro-level historical data of all tournaments (Host countries, Winners, Total Goals, Attendance).
*   **`WorldCupMatches.csv`**: Includes match-by-match statistics (Home/Away teams, Half-time scores, Match outcomes).
*   **`WorldCupPlayers.csv`**: Features micro-level player data (Line-ups, Positions, Match Events).

## 🛠️ Tech Stack & Libraries
*   **Language:** Python 3
*   **Data Manipulation:** `pandas`, `numpy`
*   **Data Visualization:** `matplotlib`, `seaborn`
*   **Environment:** Jupyter Notebook / VS Code

## 🚀 Key Objectives & Insights
1.  **Tournament Trends:** Analyzing the evolution of goal-scoring and stadium attendance over the decades.
2.  **Team Performance:** Identifying the most dominant teams and evaluating the impact of the "Home Advantage".
3.  **Player Analytics:** Breaking down match events, goals, and key player contributions across different stages of the tournament.

## 📁 Project Structure
```text
Football_Analytics_Project/
│
├── data/
│   ├── raw/                 # Original CSV files
│   └── processed/           # Cleaned data files (generated after script execution)
│
├── notebooks/               # Jupyter notebooks for EDA and prototyping
│   └── 01_basic_exploration.ipynb
│
├── src/                     # Modularized Python scripts (OOP approach)
│   ├── data_loader.py       
│   └── visualizations.py    
│
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
⚙️ How to Run the Project
Clone this repository to your local machine.

Ensure you have Python installed.

Install the required dependencies:

Bash
pip install -r requirements.txt
Navigate to the notebooks/ directory and launch Jupyter to view the step-by-step analysis.

Author: Mohsin Atta
Role: Data Analyst / Developer
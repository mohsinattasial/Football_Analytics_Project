"""Streamlit Community Cloud portfolio adapter for Football_Analytics_Project.

This does not replace the original implementation.
"""
from pathlib import Path

import streamlit as st

TITLE = "Historical World Cup Analytics"
ICON = "⚽"
DESC = "Interactive historical FIFA World Cup tournament summaries using the repository's real WorldCups.csv dataset (1930–2014)."
CATEGORY = "Data analytics"
NOTICE = "Historical dataset ends in 2014. Charts describe tournament data and do not predict results."
GITHUB = "https://github.com/mohsinattasial/Football_Analytics_Project"
VERCEL = "https://mohsin-worldcup-analytics.vercel.app"
LOCAL_COMMAND = "cd Football_Analytics_Project && python main.py"
FEATURES = ["Goals by tournament","Winner distribution","Historical host information"]

st.set_page_config(page_title=TITLE + " | Mohsin Atta", page_icon=ICON, layout="wide")
st.caption("Mohsin Atta · GitHub Portfolio · Streamlit Cloud edition")
st.title(ICON + " " + TITLE)
st.write(DESC)
st.caption(CATEGORY)

left, right = st.columns(2)
with left:
    st.link_button("GitHub source code", GITHUB, use_container_width=True)
with right:
    st.link_button("Existing browser version", VERCEL, use_container_width=True)

st.info(NOTICE)
with st.expander("Original project and features", expanded=False):
    for feature in FEATURES:
        st.write("• " + feature)
    st.code(LOCAL_COMMAND, language="bash")

import pandas as pd

data_file = Path(__file__).resolve().parents[1] / "Football_Analytics_Project" / "data" / "raw" / "WorldCups.csv"
if not data_file.exists():
    st.error("The historical CSV is missing from this repository.")
    st.stop()
@st.cache_data
def world_cups():
    return pd.read_csv(data_file)

df = world_cups()
st.subheader("Historical World Cups")
st.caption("Data source: WorldCups.csv in this repository, through 2014")
one, two, three = st.columns(3)
one.metric("Tournaments", len(df))
two.metric("Tournament goals", int(df["GoalsScored"].sum()))
three.metric("Distinct winner labels", int(df["Winner"].nunique()))
metric = st.selectbox("Metric", ["GoalsScored", "MatchesPlayed", "QualifiedTeams"],
                      format_func=lambda x: {"GoalsScored":"Goals scored","MatchesPlayed":"Matches played","QualifiedTeams":"Qualified teams"}[x])
st.bar_chart(df.set_index("Year")[metric], use_container_width=True)
st.dataframe(df[["Year", "Country", "Winner", "GoalsScored", "MatchesPlayed"]],
             use_container_width=True, hide_index=True)

st.divider()
st.caption("© 2026 Mohsin Atta · Educational portfolio · MIT-licensed original code where applicable")

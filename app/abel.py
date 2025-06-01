# app/main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils import load_clean_data, generate_summary_table  # removed unused imports
import streamlit as st
import pandas as pd

# Streamlit setup
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# Dashboard title
st.title("🌞 Cross-Country Solar Potential Dashboard")

# Sidebar controls
st.sidebar.header("Dashboard Controls")
metrics = ["GHI", "DNI", "DHI"]
selected_metric = st.sidebar.selectbox("Select Metric", metrics)

# Load data
data = load_clean_data()

# (Removed boxplot section)

# Summary table
st.subheader("📊 Summary Statistics")
sum_table = generate_summary_table(data)
st.dataframe(sum_table.style.format("{:.2f}"))

# (Removed bar plot section)

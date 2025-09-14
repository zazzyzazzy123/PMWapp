import streamlit as st
import pandas as pd

# Load rules
rules = pd.read_csv("rules.csv")

# Strip spaces from column names (important fix)
rules.columns = rules.columns.str.strip().str.lower()

st.title("Pharmacogenomic Dosing Prototype")

drug = st.selectbox("Select a drug:", rules["drug"].unique())
phenotype = st.selectbox("Select patient phenotype:", rules["phenotype"].unique())

match = rules[(rules["drug"] == drug) & (rules["phenotype"] == phenotype)]

if not match.empty:
    st.subheader("Recommendation")
    st.write(match["recommendation"].values[0])
else:
    st.warning("No rule available for this selection.")

import streamlit as st
import pandas as pd

# Load CSV
rules = pd.read_csv("rules.csv")
rules.columns = rules.columns.str.strip().str.lower()

st.title("Pharmacogenomic Dosing Prototype")

# Select drug
drug = st.selectbox("Select a drug:", rules["drug"].unique())

# Select phenotype (linked to the drug chosen)
phenotypes = rules[rules["drug"] == drug]["phenotype"].unique()
phenotype = st.selectbox("Select patient phenotype:", phenotypes)

# Lookup recommendation
match = rules[(rules["drug"] == drug) & (rules["phenotype"] == phenotype)]

st.subheader("Recommendation")
if not match.empty:
    st.success(match["recommendation"].values[0])
else:
    st.warning("⚠️ No recommendation found for this selection.")









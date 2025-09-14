import streamlit as st
import pandas as pd

# Load rules
rules = pd.read_csv("rules.csv")
rules.columns = rules.columns.str.strip().str.lower()

st.title("Pharmacogenomic Dosing Prototype")

# Select a drug
drug = st.selectbox("Select a drug:", rules["drug"].unique())

# Filter phenotypes for that drug
phenotypes_for_drug = rules[rules["drug"] == drug]["phenotype"].unique()
phenotype = st.selectbox("Select patient phenotype:", phenotypes_for_drug)

# Find matching recommendation
match = rules[
    (rules["drug"].str.strip() == drug.strip()) &
    (rules["phenotype"].str.strip() == phenotype.strip())
]

if not match.empty:
    st.subheader("Recommendation")
    st.success(match["recommendation"].values[0])
else:
    st.warning("No rule available for this selection.")







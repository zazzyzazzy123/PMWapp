import streamlit as st
import pandas as pd

# Load rules
rules = pd.read_csv("rules.csv")
rules.columns = rules.columns.str.strip().str.lower()  # clean headers

st.title("Pharmacogenomic Dosing Prototype")

drug = st.selectbox("Select a drug:", rules["drug"].unique())
phenotype = st.selectbox("Select patient phenotype:", rules["phenotype"].unique())

# Ensure clean matching
match = rules[
    (rules["drug"].str.strip() == drug.strip()) &
    (rules["phenotype"].str.strip() == phenotype.strip())
]

if not match.empty:
    st.subheader("Recommendation")
    st.write(match["recommendation"].values[0])
else:
    st.warning("No rule available for this selection.")




import streamlit as st
import pandas as pd

# Load rules
rules = pd.read_csv("rules.csv")
rules.columns = rules.columns.str.strip().str.lower()  # clean headers

st.title("Pharmacogenomic Dosing Prototype")

# Select a drug
drug = st.selectbox("Select a drug:", rules["drug"].unique())

# Filter phenotypes based on drug
phenotypes_for_drug = rules[rules["drug"] == drug]["phenotype"].unique()
phenotype = st.selectbox("Select patient phenotype:", phenotypes_for_drug)

# Match the rule
match = rules[
    (rules["drug"].str.strip() == drug.strip()) &
    (rules["phenotype"].str.strip() == phenotype.strip())
]

if not match.empty:
    st.subheader("Recommendation")
    st.write(match["recommendation"].values[0])
else:
    st.warning("No rule available for this selection.")





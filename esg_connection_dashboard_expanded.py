
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ESG Connection", layout="wide")

# Brand font + styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #324D3E;
        background-color: #F4F1EE;
    }
    .stProgress > div > div {
        background-color: #8F9779 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("ESG Connection – Client Dashboard")
st.subheader("Client: CSX Corporation | Sector: Transportation | Reporting Year: 2023")

# Load client ESG insights (pre-extracted CSV)
@st.cache_data
def load_client_data():
    return pd.read_csv("CSX_ESG_Dashboard_Insights.csv")

client_df = load_client_data()

# Tabs for structure
tab1, tab2, tab3 = st.tabs(["AlignESG", "EcoScope", "SustainTrack"])

# AlignESG Tab
with tab1:
    st.header("AlignESG – Framework Alignment & Disclosure Summary")
    st.markdown("**Summary:** CSX aligns well with ISSB and GRI frameworks, particularly in climate risk governance and emissions reduction efforts. Key disclosure gaps include Scope 3 emissions and biodiversity impact detail.")
    
    st.markdown("### ESG Disclosure Summary Table")
    st.dataframe(client_df)

    st.markdown("### ESG Ratings (AI-Assessed)")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(client_df["Topic"], client_df["Rating (out of 100)"], color="#8F9779")
    ax.set_xlabel("ESG Impact Rating")
    ax.set_title("CSX 2023 ESG Topic Ratings")
    ax.invert_yaxis()
    ax.grid(axis='x')
    st.pyplot(fig)

# EcoScope Tab
with tab2:
    st.header("EcoScope – Carbon Insights & Scope Disclosures")
    st.markdown("**Summary:** CSX discloses Scope 1 emissions effectively but lacks completeness on Scope 3. A major highlight includes 12.9M tons of CO₂ avoided via rail use versus truck freight.")
    
    st.markdown("### Emissions Breakdown (Narrative Insights)")
    st.markdown("- Scope 1: Fuel efficiency initiatives in place, positive reduction trend.")
    st.markdown("- Scope 2: Moderate progress with electrification.")
    st.markdown("- Scope 3: Still under development — currently a transparency risk.")

    st.markdown("### CO₂ Avoidance Impact")
    st.success("12.9M tons of CO₂ avoided (truck-to-rail mode shift)")

# SustainTrack Tab
with tab3:
    st.header("SustainTrack – ESG KPI Tracking & Progress")
    st.markdown("**Summary:** Strong KPIs reported in safety, DEI, and operational innovation. Continued growth in these areas contributes to positive stakeholder perception and lower ESG risk scores.")

    st.markdown("### Key Performance Indicators")
    st.metric("Personal Injury Rate", "12% ↓", "Year-over-Year")
    st.metric("CEO Approval Score", "72%", "Up from 30%")
    st.metric("Innovations Submitted", "350+", "")
    st.metric("Responder Training Events", "60+", "")

    st.markdown("### Visual GHG Goal Progress")
    st.progress(0.4, text="GHG Reduction Goal (2030)")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ESG Connection", layout="wide")

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

st.title("ESG Connection Dashboard")
st.subheader("Live ESG Insights Powered by Real Company Data")

tab1, tab2, tab3 = st.tabs(["AlignESG", "EcoScope", "SustainTrack"])

# Load CSX data
@st.cache_data
def load_csx_data():
    return pd.read_csv("CSX_ESG_Dashboard_Insights.csv")

csx_df = load_csx_data()

with tab1:
    st.header("AlignESG - Framework Alignment & Disclosure Support")
    st.markdown("### Interactive Disclosure Table (CSX 2023)")
    st.dataframe(csx_df)

    st.markdown("### ESG Insight Rating Chart")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(csx_df["Topic"], csx_df["Rating (out of 100)"], color="#8F9779")
    ax.set_xlabel("ESG Impact Rating")
    ax.set_title("CSX 2023 ESG Insight Ratings")
    ax.invert_yaxis()
    ax.grid(axis='x')
    st.pyplot(fig)

with tab2:
    st.header("EcoScope - Emissions & Carbon Insights")
    st.markdown("### CSX Scope Insight Highlights")
    st.markdown("- **Scope 1**: Emissions reduced via fuel efficiency programs")
    st.markdown("- **Scope 3**: Not yet fully disclosed (rating: 40)")
    st.markdown("- **GHG Strategy**: 12.9M tons CO₂ avoided (truck-to-rail shift)")

with tab3:
    st.header("SustainTrack - Performance KPIs")
    st.markdown("### Key ESG Performance Areas")
    st.metric("Personal Injury Rate Reduction", "12%", "- YoY")
    st.metric("CEO Approval Increase", "72%", "↑ from 30%")
    st.metric("Innovations Submitted", "350+", "")
    st.metric("Safety Training Events", "60+", "")

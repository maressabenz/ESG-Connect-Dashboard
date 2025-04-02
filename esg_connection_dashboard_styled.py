
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Brand styling
st.set_page_config(page_title="ESG Connection", layout="wide")
st.markdown("""
    <style>
    .main {
        background-color: #F4F1EE;
    }
    .stProgress > div > div {
        background-color: #8F9779 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("ESG Connection")
st.subheader("Your Central Hub for ESG Reporting, Strategy & Insights")

tab1, tab2, tab3 = st.tabs(["AlignESG", "EcoScope", "SustainTrack"])

with tab1:
    st.header("AlignESG - Framework Alignment & Disclosure Support")
    st.markdown("""
    **Quick Overview:**
    - ESG framework alignment (ISSB S1/S2, GRI)
    - Gap analysis table
    - AI-drafted disclosure text
    - Downloadable compliance summary
    """)
    st.success("Compliance Status: 68% ISSB-aligned, 74% GRI-aligned")

    st.markdown("### Disclosure Completion Table")
    data = {
        "Disclosure": ["GHG Emissions", "Climate Risks", "Board Oversight", "Scope 3", "Biodiversity"],
        "Status": ["Complete", "Complete", "Partial", "Missing", "Partial"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

    st.markdown("### Framework Radar Chart")
    labels = ['ISSB', 'GRI', 'CDP', 'TCFD']
    values = [68, 74, 55, 60]
    angles = [n / float(len(labels)) * 2 * 3.14159 for n in range(len(labels))]
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(subplot_kw={'polar': True}, facecolor='#F4F1EE')
    ax.plot(angles, values, color='#8F9779', linewidth=2, linestyle='solid')
    ax.fill(angles, values, color='#C0A98E', alpha=0.4)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='#333333')
    st.pyplot(fig)

with tab2:
    st.header("EcoScope - Emissions & Carbon Reporting")
    st.markdown("""
    **Quick Overview:**
    - Scope 1, 2, and 3 emissions tracking
    - Carbon intensity benchmarks
    - Climate scenario stress testing
    - Recommendations for reduction strategy
    """)
    scope_emissions = [2.0, 0.6, 4.5]
    fig2, ax2 = plt.subplots(facecolor='#F4F1EE')
    colors = ['#8F9779', '#C0A98E', '#A26769']
    ax2.pie(scope_emissions, labels=['Scope 1', 'Scope 2', 'Scope 3'], autopct='%1.1f%%', colors=colors)
    ax2.axis('equal')
    st.pyplot(fig2)

    st.markdown("### Year-over-Year GHG Emissions")
    st.line_chart({"2021": [2.4, 0.7], "2022": [2.1, 0.6], "2023": [2.0, 0.6]})

with tab3:
    st.header("SustainTrack - ESG KPIs & Roadmap Progress")
    st.markdown("""
    **Quick Overview:**
    - Sustainability targets (Energy, DEI, Waste, etc.)
    - Progress bars and trend visualizations
    - Timeline to compliance goals
    - Monthly report download
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Workforce Diversity", "38%", "Target: 50% by 2025")
        st.progress(0.38, text="DEI Progress")
    with col2:
        st.metric("Safety Incidents (YTD)", "12", "-20% from last year")
        st.progress(0.8, text="Safety Goal")

    st.markdown("### GHG Reduction Goal Progress")
    st.progress(0.4, text="GHG Reduction Goal 2030")

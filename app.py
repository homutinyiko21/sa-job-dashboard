import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SA Job Intelligence Dashboard",
    layout="wide"
)

# Load data
df = pd.read_csv("jobs.csv")

# Header
st.title("🇿🇦 South African Job Intelligence Dashboard")
st.caption("Executive Hiring Trends | Built with Python & Streamlit")

# KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Jobs", len(df))

with col2:
    st.metric("Avg Salary", f"R{round(df['salary'].mean(),0):,.0f}")

with col3:
    st.metric("Top City", df["city"].mode()[0])

with col4:
    st.metric("Top Employer", df["company"].mode()[0])

st.divider()

# Charts
left, right = st.columns(2)

with left:
    st.subheader("Jobs by City")
    st.bar_chart(df["city"].value_counts())

with right:
    st.subheader("Average Salary by City")
    st.bar_chart(df.groupby("city")["salary"].mean())

st.divider()

# Table
st.subheader("Recruitment Dataset")
st.dataframe(df, use_container_width=True)

# Insights
st.subheader("Executive Insight")
highest = df.loc[df["salary"].idxmax()]
st.success(
    f"Highest paying opportunity: {highest['title']} at {highest['company']} "
    f"in {highest['city']} paying R{highest['salary']:,}"
)

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Job Dashboard",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Job Dashboard")

# Load Excel file
df = pd.read_excel("jobs.xlsx")

st.sidebar.header("🔎 Search Jobs")

# Job Title filter
job_titles = ["All"] + sorted(
    df["JOB TITLE"].dropna().unique().tolist()
)

selected_job = st.sidebar.selectbox(
    "Job Title",
    job_titles
)

# Company filter
companies = ["All"] + sorted(
    df["COMPANY NAME"].dropna().unique().tolist()
)

selected_company = st.sidebar.selectbox(
    "Company",
    companies
)

# Industry filter
industries = ["All"] + sorted(
    df["INDUSTRY"].dropna().unique().tolist()
)

selected_industry = st.sidebar.selectbox(
    "Industry",
    industries
)

# Location filter
locations = ["All"] + sorted(
    df["LOCATION"].dropna().unique().tolist()
)

selected_location = st.sidebar.selectbox(
    "Location",
    locations
)

# Apply filters
if selected_job != "All":
    df = df[df["JOB TITLE"] == selected_job]

if selected_company != "All":
    df = df[df["COMPANY NAME"] == selected_company]

if selected_industry != "All":
    df = df[df["INDUSTRY"] == selected_industry]

if selected_location != "All":
    df = df[df["LOCATION"] == selected_location]

# Dashboard metric
st.metric("Total Jobs", len(df))

# Display jobs
st.subheader("📋 Available Jobs")

st.dataframe(
    df,
    width="stretch"
)



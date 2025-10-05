import streamlit as st
import pandas as pd
import glob
import os

st.set_page_config(page_title="Groundwater Depletion Dashboard", layout="wide")

st.title("Groundwater Depletion Dashboard - India")

# Load all groundwater CSV files
files = glob.glob("groundwater_extracted/*.csv")

if not files:
    st.error("No groundwater files found! Make sure the CSVs are inside 'groundwater_extracted' folder.")
else:
    # Let user pick a file
    selected_file = st.selectbox("Select a groundwater dataset", files)

    # Read CSV safely
    try:
        df = pd.read_csv(selected_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    st.subheader("Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    # Auto-detect groundwater depletion column
    # Based on previous analysis, 'lwe' and 'lwe_mm' are relevant columns
    possible_cols = [col for col in df.columns if "lwe" in col.lower()]

    if possible_cols:
        col = st.selectbox("Choose groundwater depletion column", possible_cols)

        st.subheader(f"Visualization - {col}")

        # Layout for charts
        col1, col2 = st.columns(2)

        with col1:
            st.line_chart(df[col], height=300)

        with col2:
            st.bar_chart(df[col], height=300)

        st.subheader("Summary Statistics")
        st.write(df[col].describe())

        # Optional: date-based trend if date column exists
        date_cols = [c for c in df.columns if "date" in c.lower()]
        if date_cols:
            date_col = date_cols[0]
            try:
                df[date_col] = pd.to_datetime(df[date_col])
                df = df.sort_values(by=date_col)
                st.subheader("Time Trend")
                st.line_chart(df.set_index(date_col)[col])
            except:
                st.warning("Couldn't parse date column for trend chart.")
    else:
        st.warning("No groundwater depletion column found in this file.")




st.set_page_config(page_title="Rainfall Data Dashboard", layout="wide")

st.title("Rainfall Data Dashboard - India")

# Load all rainfall CSV files
files = glob.glob("rainfall_extracted/*.csv")

if not files:
    st.error("No rainfall files found! Make sure the CSVs are inside 'rainfall_extracted' folder.")
else:
    # Let user pick a file
    selected_file = st.selectbox("Select a rainfall dataset", files)

    # Read CSV safely
    try:
        df = pd.read_csv(selected_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    st.subheader("Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    # Auto-detect precipitation column
    possible_cols = [col for col in df.columns if "precip" in col.lower() or "rain" in col.lower()]

    if possible_cols:
        col = st.selectbox("Choose rainfall column", possible_cols)
        
        st.subheader(f"Visualization - {col}")
        
        # Layout for charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.line_chart(df[col], height=300)
        
        with col2:
            st.bar_chart(df[col], height=300)

        st.subheader("Summary Statistics")
        st.write(df[col].describe())

        # Optional: date-based trend if date column exists
        date_cols = [c for c in df.columns if "date" in c.lower()]
        if date_cols:
            date_col = date_cols[0]
            try:
                df[date_col] = pd.to_datetime(df[date_col])
                df = df.sort_values(by=date_col)
                st.subheader("Time Trend")
                st.line_chart(df.set_index(date_col)[col])
            except:
                st.warning("Couldn't parse date column for trend chart.")
    else:
        st.warning("No precipitation column found in this file.")
#This file combines the methods from data and plotting in order to display the data online IOT be displayed via streamlit
import fastf1
import streamlit as st
from data import load_session, get_driver_laps, get_pit_laps
from plotting import plot_driver_laps
fastf1.Cache.enable_cache('f1_cache')

st.set_page_config(page_title="F1 Dashboard", layout="wide")
st.title("F1 Dashboard")

#Dropdown bar w/ static options
col1, col2, col3, col4 = st.columns(4)

with col1:
    year = st.selectbox("Year", options=[2023, 2024, 2025])
with col2:
    gp = st.selectbox("Grand Prix", options=["Monza", "Spa", "Silverstone"])
with col3:
    session_type = st.selectbox("Session", options=["FP1", "FP2", "FP3", "Q", "R"])
with col4:
    driver = st.selectbox("Driver", options=["LEC", "VER", "HAM", "NOR", "PIA"])

#Load + plot
if st.button("Generate Plot"):
    with st.spinner("Loading session data..."):
        session = load_session(year, gp, session_type)
        laps = get_driver_laps(session, driver)
        pit_in_laps, pit_out_laps = get_pit_laps(laps)
        fig = plot_driver_laps(laps, pit_in_laps, pit_out_laps, driver, year, gp, session)

        st.pyplot(fig)
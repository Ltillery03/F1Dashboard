# F1 Snapshot Dashboard
Interactive Streamlit dashboard for exploring Formula 1 race data. Contains lap times, tire strategy, and pit stops for the selected driver in a given session

[INSERT IMAGE HERE]

WHAT IT DOES

-Pulls session data using FastF1

-Plots lap times across a race, color coded by tire compound

-Marks pit stop entry/exit laps directly on the chart

-Overlays rolling average trendline per stint to show pace evolution

TECH STACK

-Python

-FastF1

-Streamlit

-pandas

-seaborn/matplotlib

RUNNING LOCALLY

1. Clone Repo and install dependencies
pip install -r requirements.txt
2. Run the app
streamlit run app.py
3. Select year, Grand Prix, session, and driver, then click Generate Plot
    *Note the first load for any session will be slower since FastF1 downloads and caches timing data the first time it's requested

STRUCTURE

├── app.py        # Streamlit UI: dropdowns, layout, page logic

├── data.py        # FastF1 data loading and transformation functions

├── plotting.py     # seaborn/matplotlib chart generation

└── requirements.txt

CURRENT SCOPE

This version is fixed in terms of years, Grand Prix, and drivers listed in the dropdowns. The planned V2 will make these dynamic, pulling actual event schedule and session participation from FastF1 so any year/GP/driver combination is selectable

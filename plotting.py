#This file plots the data taken from the data.py file
import fastf1
import fastf1.plotting
import data
import seaborn as sns
from matplotlib import pyplot as plt

def plot_driver_laps(laps, pit_in_laps, pit_out_laps, driver, year, gp, session):
    color_compound = fastf1.plotting.get_compound_mapping(session=session)
    race_laps = laps[laps['PitInTime'].isna() & laps['PitOutTime'].isna()]

    fig, ax = plt.subplots()

    #create the scatter plot using all not pit entry/exit laps
    sns.scatterplot(data=race_laps, x="LapNumber", y="LapTimeSeconds", ax=ax,
                    hue="Compound", palette=color_compound)
    
    #mark pit entry and exit
    for lap in pit_in_laps:
        ax.axvline(x=lap, linestyle="--", color="red", linewidth=1.2)
    for lap in pit_out_laps:
        ax.axvline(x=lap, linestyle="--", color="green", linewidth=1.2)

    #create trendline for each stint
    for stint_num, stint_laps in race_laps.groupby("Stint"):
        rolling_avg = stint_laps['LapTimeSeconds'].rolling(window=3).mean()
        ax.plot(stint_laps['LapNumber'], rolling_avg, color='cyan')

    #readability
    ax.set_title(f"{driver} - {year} {gp} ({session.name})")
    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time (s)")

    return fig
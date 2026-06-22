from data import load_session, get_driver_laps, get_driver_stints, get_pit_laps
from plotting import plot_driver_laps
import matplotlib.pyplot as plt

YEAR = 2024
GP = "Monza"
SESSION_TYPE = "R"
DRIVER = "LEC"

print(f"Loading {YEAR} {GP} {SESSION_TYPE}...")
session = load_session(YEAR, GP, SESSION_TYPE)

laps = get_driver_laps(session, DRIVER)
pit_in_laps, pit_out_laps = get_pit_laps(laps)

print("Generating plot...")
fig = plot_driver_laps(laps, pit_in_laps, pit_out_laps, DRIVER, YEAR, GP, session)

plt.show()
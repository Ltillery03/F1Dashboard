from data import load_session, get_session_drivers, get_driver_laps, get_driver_stints, get_pit_laps

# --- Config: pick a known session to test against ---
YEAR = 2024
GP = "Monza"
SESSION_TYPE = "R"
DRIVER = "LEC"  # Abbreviation, e.g. 'LEC', 'VER', 'HAM'

print(f"Loading {YEAR} {GP} {SESSION_TYPE}...")
session = load_session(YEAR, GP, SESSION_TYPE)

print("\n--- Drivers in session ---")
print(get_session_drivers(session))

print(f"\n--- Laps for driver: {DRIVER} ---")
laps = get_driver_laps(session, DRIVER)
print(laps[['LapNumber', 'LapTime', 'Stint', 'Compound', 'PitInTime', 'PitOutTime']])

print(f"\n--- Stints for {DRIVER} ---")
stints = get_driver_stints(laps)
for stint_num, stint_laps in stints:
    print(f"Stint {stint_num}: laps {stint_laps['LapNumber'].min()}-{stint_laps['LapNumber'].max()}, "
          f"compound={stint_laps['Compound'].iloc[0]}, lap count={len(stint_laps)}")

print(f"\n--- Pit laps for {DRIVER} ---")
pit_in, pit_out = get_pit_laps(laps)
print("Pit IN laps:", pit_in.tolist())
print("Pit OUT laps:", pit_out.tolist())
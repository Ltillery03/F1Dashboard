#This file gets the necessary data to display in the plot. Session, driver name and driver laps for each participant in a session
import fastf1

def load_session(year, gp, session_type):
    session = fastf1.get_session(year, gp, session_type) #gets the specified session from a desired gp
    session.load()
    return session

def get_session_drivers(session):
    return session.results[['DriverNumber','FullName','Abbreviation']] #returns list of drivers in a given session 

def get_driver_laps(session, driver):
    laps = session.laps.pickdrivers(driver)
    return laps #returns laps of a given driver

def get_driver_stints(laps):
    return laps.groupby('Stint') #returns the laps grouped by stint number

def get_pit_laps(laps):
    pit_in_laps = laps.loc[laps['PitInTime'].notna(), 'LapNumber']
    pit_out_laps = laps.loc[laps['PitOutTime'].notna(), 'LapNumber']
    return pit_in_laps, pit_out_laps #returns the lap numbers where the pits were entered/exited
"""
This file is for me to explore pyergast and its features to gain insight for the analysis. 
"""
import numpy as np
import pandas as pd
from pyergast import pyergast

"""
Basic Queries
"""

# DATAFRAME OF ALL DRIVERS
all_drivers_df = pyergast.get_drivers()

# DATAFRAME OF ALL CONSTRUCTORS
all_cons_df = pyergast.get_constructors()

# DATAFRAME OF ALL RACE RESULTS
race_results_df = pyergast.get_race_result()

# DATAFRAME OF ALL QUALI RESULTS
quali_results_df = pyergast.get_qualifying_result()

# DATAFRAME OF SEASON SCHEDULES
season_schedule_21 = pyergast.get_schedule(2021)

# DATAFRAME OF DRIVERS STANDINGS
d_standings = pyergast.driver_standings()

#DATAFRAME OF CONSTRUCTORS STANDINGS
c_standings = pyergast.constructor_standings()

# QUERY ID
HAM_id = pyergast.find_driverid("lewis", "hamilton")
RB_id = pyergast.find_constructorid("Red Bull")
spain_cid = pyergast.find_circuitid("Spain")

"""
Snapshot queries
"""
# SNAPSHOT OF JOHN ALESI
j_alesi_snap = pyergast.query_driver('alesi')

# SNAPSHOT OF JORDAN F1 TEAM
jordan_snap = pyergast.query_constructor('jordan')
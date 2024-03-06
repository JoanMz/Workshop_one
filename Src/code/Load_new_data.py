import sys
sys.path.append(r"../../Sql_connection")
import postgres_connect #that library is for connect with my postgres database using the engine(connector) of sql_alchemy 
from decouple import config
from matplotlib import gridspec
import numpy as np #for math
import pandas as pd #for data handle 
import matplotlib.pyplot as plt #for viz
import re

def determine_hire_state(row):
    if row['Code Challenge Score'] >= 7 and row['Technical Interview Score'] >= 7:
        return 1
    else:
        return 0


if __name__ == "__main__":
    path = ""
    hired_table =  pd.read_csv(f"{path}")#set_the_path_of_the_data
    hired_table["Hired"] = hired_table.apply(determine_hire_state, axis=1).astype(int) #add the colum with the constraint axis=1 for do entry by entry
    hired_table.to_sql(f"{config("DB_TABLE2")}", con=postgres_connect.connection(), if_exists="append", index=False) #load into postgres append for no remove old registers
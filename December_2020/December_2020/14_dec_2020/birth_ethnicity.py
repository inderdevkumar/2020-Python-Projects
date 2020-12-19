import pandas as pd
import matplotlib.pyplot as plt
import re

births_data= "births.csv"

ethnicities = {"asian and paci" : "asian and pacific islander", "black non hisp":"black non hispanic","white non hisp":"white non hispanic"}

def clean_csv(file_name, ethnicities):
    for ethnicity in ethnicities:
        with open(file_name,'r') as file:
            filedata = file.read()
            filedata = re.sub(r"\b" + ethnicity +  r"\b" , ethnicities[ethnicity], filedata)
        with open(file_name,'w') as file:
            file.write(filedata)


clean_csv(births_data, ethnicities)

names = ["birth_year", "gender", "ethnicity", "first_name", "frequency"]

births = pd.read_csv(births_data, names=names, header = 0)

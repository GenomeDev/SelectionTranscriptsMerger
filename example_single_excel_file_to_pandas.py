import pandas as pd
import os

file_basepath = "data" # pot od root folder do mape, kjer so shranjene datoteke
filename = "Selection_1_transcript_stats.csv" # ime datoteke

filepath = os.path.join(file_basepath, filename) # združi file_basepath in filename (npr. data/Selection_1_transcript_stats.csv)

# data = pd.read_excel('filename.xlsm', sheetname=0) # can also index sheet by name or fetch all sheets
data = pd.read_csv(filepath, comment="#", skiprows=3)
print(data)

# ** RAZLAGA **
# Določimo novo spremenljivko z imenom data, ki ji priredimo vrednost, ki jo vrne funkcija pd.read_csv(FILE).
# Na internetu pogledamo kaj ta funkcija naredi: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# in vidimo, da vrne objekt tipa DataFrame (lahko tudi pogledaš na netu kaj je to). 
# Torej je spremenljivka data objekt tipa DataFrame, na katerem lahko izvedemo nadaljnje funkcije / iskanje po stolpcih itd.

# prevedi vrednosti v stolpcu v list
# data[IME-STOLPCA].tolist(); funkcijo tolist() na objektu data (ki je objekt tipa DataFrame, )
list_geni = data["Gene"].tolist() 
list_counts = data["Count"].tolist()
list_density = data["Density (µm^-2)"].tolist()

# prikaži vrednosti listov
print(list_geni)
print(list_counts)
print(list_density)

print("Finished.")
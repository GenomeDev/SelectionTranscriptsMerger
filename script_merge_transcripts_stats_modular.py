import pandas as pd
import os

# Define initial values
SKIPROWS = 3 # count of initial rows to skip in csv files
COMMENT = "#"
BASE_DATAFILE_PATH = "data"
FILENAME_MODULAR = "Selection_%_transcript_stats.csv"
FILE_COUNT = -1
_COLUMNS = ["Gene","Count","Density (µm^-2)"]

# OUTPUT FILENAME
OUT_FILENAME = "results.xlsx"
OUT_SHEETNAME = "Results"

def parse_csv_table_file(filepath, column_names:list, skiprows=3, comment="#"):
    """
    Parses csv file containing a table to return the dictionary matching supplied column_names.
    If column_names is ["ColA", "ColB", "ColC"], then the returned dictionary is:
    {
        "ColA":[list of values in column with name ColA],
        "ColB":[list of values in column with name ColB],
        "ColC":[list of values in column with name ColC]
    }
    """
    result = dict()
    data = pd.read_csv(filepath, skiprows=skiprows, comment=comment)
    print(data)
    for colname in column_names:
        values = data[colname].tolist()
        result[colname] = values
    return result 

def parse_selection_transcript_stats(filepath, column_names:list=_COLUMNS, skiprows=3, comment="#"):
    """
    Return the following dictionary after parsing filepath (csv of selection transcripts):
    {
        "Gene":[list of genes],
        "Count":[list of counts],
        "Density (µm^-2)":[list of densities]
    }
    """
    return parse_csv_table_file(filepath=filepath, column_names=column_names, skiprows=skiprows, comment=comment)
    


# *** start of the program ***

# Ask the user to supply file count
FILE_COUNT = int(input("Število datotek - vstavi številko in pritisni ENTER:"))
genes = [] # lista genov
densities = dict() # slovar med številko vzorca in listo gostot

# preberi vse datoteke in posodobi densities slovar in listo genov
for i in range(1,FILE_COUNT+1):
    current_filename = FILENAME_MODULAR.replace("%", str(i))
    current_filepath = os.path.join(BASE_DATAFILE_PATH, current_filename)
    parsed = parse_selection_transcript_stats(current_filepath, skiprows=SKIPROWS, comment=COMMENT)
    parsed_densities = [float(value) for value in parsed["Density (µm^-2)"]]
    densities[i] = parsed_densities
    if genes == []:
        genes = parsed["Gene"]

# pretvori genes (lisa genov) in densities slovar v pandas DataFrame
df = pd.DataFrame(index=genes)

# Iterate over the dictionary and add each list of density values as a new column in the DataFrame
for i,dens in densities.items():
    df[i] = dens

print(df)

df.to_excel(OUT_FILENAME, sheet_name=OUT_SHEETNAME)

print(f"Finished and saved to {OUT_FILENAME}.")
    
    

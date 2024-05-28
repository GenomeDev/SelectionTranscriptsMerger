(1) Install Python and pip (glej Navodila.docx)

(2) Install the following pip packages:

2.1
```
pip install pandas
```

2.2
```
pip install xlsxwriter
```

(3) Create a local "root" folder (any folder designated as the main folder for the "project"), create a subfolder called `data` and store the selection transcript data files inside the 
data folder using the `Selection_X_transcript_stats.csv` naming convention. 

(4) Download and save `script_merge_transcript_stats.py` from this repository into the root folder, so that the file structure is as follows:
```
C:/.../root/
  - data/
      - Selection_1_transcript_stats.csv
      - Selection_2_transcript_stats.csv
      - ...
  - script_merge_transcript_stats.py
```

(5) Open CMD, move to the "root" folder (**cd [PATH_TO_ROOT_FOLDER]**) and execute the script using the command **python script_merge_transcript_stats.py**. A results excel file
should be created inside the root folder.

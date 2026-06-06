import pandas as pd
from pathlib import Path

#Loading the CSV file containing the extracted eGeMAPS features
df = pd.read_csv("daic_B5_egemaps_features.csv")

#Function that extracts the participant's ID from the file path
#For: data/audio/307/307_2.wav
#Return: "307" (the name of the parent folder)
def extract_speaker(path_str):
    p = Path(path_str)
    return p.parent.name

#Function that extracts the name of the audio file from the full path
#For: data/audio/307/307_2.wav
#Return: "307_2.wav"
def extract_turn(path_str):
    return Path(path_str).name

#Create two new columns: speaker_id and turn_file
#Apply the extract_speaker function to each row in the “file” column and,
#Stores the result (the participant's ID) in a new column named “speaker_id”
df["speaker_id"] = df["file"].apply(extract_speaker)
df["turn_file"] = df["file"].apply(extract_turn)

#Move columns to the front: “speaker_id” and “turn_file” are moved to the first and second positions,
#and the other columns (eGeMAPS features) follow in their original order
cols = ["speaker_id", "turn_file", "file"] + [c for c in df.columns if c not in ["speaker_id","turn_file","file"]]
df = df[cols]

#Save the new .csv file
df.to_csv("output/daic_B5_eGeMAPS_with_ids.csv", index=False)

#Print the first few rows of the new DataFrame to verify that the new columns have been added correctly
print("Added speaker_id and turn_file columns")
print(df[["speaker_id","turn_file"]].head())
import opensmile
import pandas as pd
import os

#Path to the folder containing the .wav audio files
AUDIO_DIR = "data/audio"

#Path to the output .csv file
OUTPUT_PATH = "output/daic_B5_egemaps_features.csv"

#Initialize the OpenSMILE extractor with the eGeMAPS feature set and functionals level
#We extract the feature parameters (88 in total) from the entire turn
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

#Create a list containing the features extracted for each audio file
all_features = []

#Walk through the audio directory and process each .wav file
for root, _, files in os.walk(AUDIO_DIR):
    for filename in files:
        if filename.endswith(".wav"):   #Processes only .wav audio files
            filepath = os.path.join(root, filename)     #Building the full path to the file
            print(f"Processing {filepath}...")
            features = smile.process_file(filepath)   #Extraction of the 88 eGeMAPS features for this audio file
            features["file"] = filepath     #Add the file path as a column to identify each turn in the final .csv file
            all_features.append(features)   #Add the features in this file to the all_features list

#Combining all DataFrames into a single DataFrame
df = pd.concat(all_features)

#Save the combined DataFrame to a .csv file
df.to_csv(OUTPUT_PATH, index=False)

print("GeMAPS extraction finished!")
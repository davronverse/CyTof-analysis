import os
import flowkit as fk
import pandas as pd

def load_fcs_file(file_path):
    sample = fk.Sample(file_path)
    data = sample.dataframe
    return data

# Directory containing FCS files
directory = '/'
fcs_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.fcs')]

all_data = []
for file in fcs_files:
    data = load_fcs_file(file)
    all_data.append(data)

print(all_data)

combined_data = pd.concat(all_data, ignore_index=True)


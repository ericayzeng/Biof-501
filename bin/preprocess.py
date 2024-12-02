import pandas as pd
from sklearn.preprocessing import StandardScaler
import sys

# csv_path = './data/Fouladirad_FISH_SSPI.csv'
# out_path = './data/preprocessed_sspi_data.csv'

# Command-line arguments for input and output paths
csv_path = sys.argv[1]
out_path = sys.argv[2]

# load csv and extract columns and data
data = pd.read_csv(csv_path)
id_column = 'Subj_ID'
patient_ids = data[id_column]
sspi_columns = [col for col in data.columns if col.startswith('SSPI')]
sspi_data = data[sspi_columns]

# check for missing values
if sspi_data.isnull().any().any():
    print("Missing values found. Filling missing values with column mean.")
    exit()

# standardize the SSPI data
scaler = StandardScaler()
sspi_scaled = scaler.fit_transform(sspi_data)

# convert to df and save to file
sspi_scaled_df = pd.DataFrame(sspi_scaled, columns=sspi_columns)
sspi_scaled_df[id_column] = patient_ids
sspi_scaled_df.to_csv(out_path, index=False)

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import sys

# preprocessed_path = './data/preprocessed_sspi_data.csv'
# out_path = './data/pca_results.csv'

preprocessed_path = sys.argv[1]
out_path = sys.argv[2]

# load preprocessed data and remove ids
data = pd.read_csv(preprocessed_path)
id_column = 'Subj_ID'
patient_ids = data[id_column]
sspi_data = data.drop(columns=[id_column])

# hyperparameter to enable graphing
n_components = 3

# initialize PCA
pca = PCA(n_components=n_components)
pca_result = pca.fit_transform(sspi_data)

# convert PCA to df and save to file
pca_columns = [f'PC{i+1}' for i in range(pca_result.shape[1])]
pca_df = pd.DataFrame(pca_result, columns=pca_columns)
pca_df[id_column] = patient_ids  # add back ids
pca_df.to_csv(out_path, index=False)

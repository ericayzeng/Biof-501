import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# path to PCA results from pca.py
pca_path = sys.argv[1]
# path to preprocessed data from preprocess.py
preprocessed_path = sys.argv[2]
# path to output
out_path = sys.argv[3]

# STEP 1: load PCA data and remove ids
data = pd.read_csv(pca_path)
id_column = 'Subj_ID'
patient_ids = data[id_column]
pca_data = data.drop(columns=[id_column])

# STEP 2: find optimal cluster count
inertia = []
range_n_clusters = range(1, 20)  # test 1 to 20 clusters
for k in range_n_clusters:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pca_data)
    inertia.append(kmeans.inertia_)

# plot inertia to determine best cluster number
plt.figure(figsize=(8, 6))
plt.plot(range_n_clusters, inertia, marker='o', linestyle='-')
plt.title('Inertia based on number of clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.xticks(range_n_clusters)
plt.grid()
plt.savefig('kmeans.png')

# STEP 3: use k-means with optimal cluster number (from step 2)
optimal_clusters = 6
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
clusters = kmeans.fit_predict(pca_data)

# STEP 4: save output as map of patient ids to cluster number
patient_cluster_mapping = pd.DataFrame({
    id_column: patient_ids,
    'Cluster': clusters
})
patient_cluster_mapping.to_csv(out_path, index=False)

# 3D plot of clusters
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(
    pca_data.iloc[:, 0], 
    pca_data.iloc[:, 1],
    pca_data.iloc[:, 2],
    c=clusters,
    cmap='viridis',
    s=50
)

ax.set_title('3D K-Means Clustering')
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
plt.colorbar(scatter, label='Cluster')
plt.savefig('kmeans_3d.png')

# heatmap of clusters and SSPI
preprocessed_data = pd.read_csv(preprocessed_path)
sspi_columns = [col for col in preprocessed_data.columns if col.startswith('SSPI')]
preprocessed_data[id_column] = patient_ids
preprocessed_data['Cluster'] = clusters
cluster_centroids = preprocessed_data.groupby('Cluster')[sspi_columns].mean()

plt.figure(figsize=(12, 8))
sns.heatmap(cluster_centroids, cmap='coolwarm', cbar=True)
plt.title('Heatmap of Cluster Centroids for SSPI Indices')
plt.xlabel('SSPI Indices')
plt.ylabel('Clusters')
plt.savefig('kmeans_sspi_heatmap.png')
# Biof-501 Exploring Patient Groupings in Social and Symptom Problem Index (SSPI) Rankings

## Repository Contents
### Directories
- `bin`: Contains all the python scripts that are used in the pipeline
- `input`: Contains the input data for the pipeline
- `images`: Contains the images that are used in the README

### Files
- `dockerfile`: 
- `makefile`: 
- `workflow.nf`: The primary pipeline file that provides the instructions for executing the pipeline using Nextflow
- `nextflow.config`: Configuration file for Nextflow.

## Background
Schizophrenia is a psychiatric disorder characterized by positive symptoms, negative symptoms, and cognitive impairments. [1] Positive symptoms consist of delusions, hallucinations, and disorganized speech and behavior. [1] Negative symptoms may consist of non-verbal expression, low expression, etc. [2] To measure these symptoms, typically a Signs and Symptoms of Psychotic Illness (SSPI) rating scale is used. The SSPI is a 20-item rating scale design to measure the severity of the major symptoms in psychotic disorders. [3] The scores range from 0 (absent) to 4 (severe). The first 19 items measure the major signs and symptoms while item 20 assesses insight. [4]

The purpose of clustering SSPI data is to uncover meaningful patterns and subgroups in individuals with schizophrenia. Firstly, it provides valuable insights into symptom heterogeneity. By grouping patients with similar symptom profiles, clustering has the potential to uncover distinct phenotypes, such as those with severe delusions or cognitive impairments. Secondly, these clusters have the potential to inform more personalized treatment strategies by identifying targeted interventions that are tailored to specific symptoms. For example cognitive behavioral therapy can be recommended to patients who suffer more from delusions and cognitive remediation therapy can be recommended to those who have more cognitive impairments. Finally, clustering helps researchers better understand and categorize patients, making it easier to explore how their symptoms relate to specific research findings. This deeper understanding of schizophrenia can lead to more effective studies and treatments.

In this pipeline, we are using SSPI from 70 participants with schizophrenia in order to gain insights into symptom patterns, and identify distinct subgroups. This dataset is from a published 2022 study. Patients with psychosis were recruited through Vancouver Coastal Health mental health teams, psychiatric hospitals, and community health agencies. The sample consisted of 70 participants in the schizophrenia group. 

A pipeline is crucial for this analysis because it ensures the systematic, efficient, and reproducible processing of SSPI data.

![Untitled presentation (2)](https://github.com/user-attachments/assets/ee7d05d1-4d7b-489d-b8eb-d9f4e2680331)

## Usage

## Input Data

## Output Data
Results will be published in the `output` directory. The `output` directory will contain the intermediate datasets, and final outputs. The desired outputs for this project are as follows:
- `Preprocessed_Fouladirad_FISH_SSPI.csv`: A CSV of cleaned and standardized SSPI data ready for analysis
- `Pca_results.csv`: A CSSV of PCA-transformed data with principal components and participant IDs
- `Kmeans_results.csv`: A csv mapping participant IDs to their K-means cluster assignments
- `Kmeans_3d.png` : A 3D scatter plot showing K-means clusters in PCA-reduced space
- `Kmeans_sspi_heatmap.png`: A heatmap showing the average SSPI scores for each cluster
- `kmeans.png`: An intertia plot for determining the optimal number of clusters 

### PCA
In the PCA step of the pipeline, Principal Component Analysis (PCA) is applied to the preprocessed SSPI dataset to reduce dimensionality and identify patterns in the data. Three principal components are generated, capturing the key variability in symptom rankings while preserving essential information. The output includes a CSV file containing the transformed data with components labeled `PC1`, `PC2`, and `PC3`, along with subject IDs for reference. These results are saved in the specified ‘output’ directory and serve as a foundation for further visualization or clustering analysis.

### Clustering
In the clustering step of the pipeline, K-means clustering is applied to the PCA-transformed SSPI dataset to group patients based on their symptom profiles. An optimal number of clusters is determined by analyzing the inertia across a range of cluster values, with the final clustering performed using 6 clusters. The output includes a CSV file mapping patient IDs to their respective cluster assignments. Additionally, the results are visualized through a 3D scatter plot of the clusters based on the principal components and a heatmap showing the centroids of each cluster across SSPI indices. These ‘outputs’ are saved in the results directory for further analysis and interpretation.

![kmeans_3d](https://github.com/user-attachments/assets/54fdcd11-8f31-442c-aefa-79601ddf84d4)

![kmeans_sspi_heatmap](https://github.com/user-attachments/assets/1b3f4287-23b8-4050-aaff-9a03eb87ce81)

![kmeans](https://github.com/user-attachments/assets/178c7f73-c280-45c0-9ef5-d3e3944bc0e6)

## Container
In the pipeline, a custom Docker ....

## References
1. Rahman T, Lauriello J. Schizophrenia: An Overview. Focus (Am Psychiatr Publ). 2016;14(3):300-307. doi:10.1176/appi.focus.20160006
2. Kaneko K. Negative Symptoms and Cognitive Impairments in Schizophrenia: Two Key Symptoms Negatively Influencing Social Functioning. Yonago Acta Med. 2018;61(2):91-102. doi:10.33160/yam.2018.06.001
3. Fouladirad S, Chen LV, Roes M, et al. Functional brain networks underlying probabilistic reasoning and delusions in schizophrenia. Psychiatry Res Neuroimaging. 2022;323:111472. doi:10.1016/j.pscychresns.2022.111472
4. Liddle PF, Ngan ETC, Duffield G, Kho K, Warren AJ. Signs and Symptoms of Psychotic Illness (SSPI): A rating scale. British Journal of Psychiatry. 2002;180(1):45-50. doi:10.1192/bjp.180.1.45

# Biof-501 Exploring Patient Groupings in Social and Symptom Problem Index (SSPI) Rankings

## Background
Schizophrenia is a psychiatric disorder characterized by positive symptoms, negative symptoms, and cognitive impairments. [Lauriello] Positive symptoms consist of delusions, hallucinations, and disorganized speech and behavior. [Lauriello] Negative symptoms may consist of non-verbal expression, low expression, etc. [Kaneko] To measure these symptoms, typically a Signs and Symptoms of Psychotic Illness (SSPI) rating scale is used. The SSPI is a 20-item rating scale design to measure the severity of the major symptoms in psychotic disorders. [Fouladirad] The scores range from 0 (absent) to 4 (severe). The first 19 items measure the major signs and symptoms while item 20 assesses insight. [Liddle]

The purpose of clustering SSPI data is to uncover meaningful patterns and subgroups in individuals with schizophrenia. Firstly, it provides valuable insights into symptom heterogeneity. By grouping patients with similar symptom profiles, clustering has the potential to uncover distinct phenotypes, such as those with severe delusions or cognitive impairments. Secondly, these clusters have the potential to inform more personalized treatment strategies by identifying targeted interventions that are tailored to specific symptoms. For example cognitive behavioral therapy can be recommended to patients who suffer more from delusions and cognitive remediation therapy can be recommended to those who have more cognitive impairments. Finally, clustering helps researchers better understand and categorize patients, making it easier to explore how their symptoms relate to specific research findings. This deeper understanding of schizophrenia can lead to more effective studies and treatments.

In this pipeline, we are using SSPI from 70 participants with schizophrenia in order to gain insights into symptom patterns, and identify distinct subgroups. This dataset is from a published 2022 study. Patients with psychosis were recruited through Vancouver Coastal Health mental health teams, psychiatric hospitals, and community health agencies. The sample consisted of 70 participants in the schizophrenia group. 

A pipeline is crucial for this analysis because it ensures the systematic, efficient, and reproducible processing of SSPI data.

## Output
Results will be published in the `output` directory. 

### PCA
In the PCA step of the pipeline, Principal Component Analysis (PCA) is applied to the preprocessed SSPI dataset to reduce dimensionality and identify patterns in the data. Three principal components are generated, capturing the key variability in symptom rankings while preserving essential information. The output includes a CSV file containing the transformed data with components labeled `PC1`, `PC2`, and `PC3`, along with subject IDs for reference. These results are saved in the specified ‘output’ directory and serve as a foundation for further visualization or clustering analysis.

### Clustering
In the clustering step of the pipeline, K-means clustering is applied to the PCA-transformed SSPI dataset to group patients based on their symptom profiles. An optimal number of clusters is determined by analyzing the inertia across a range of cluster values, with the final clustering performed using 6 clusters. The output includes a CSV file mapping patient IDs to their respective cluster assignments. Additionally, the results are visualized through a 3D scatter plot of the clusters based on the principal components and a heatmap showing the centroids of each cluster across SSPI indices. These ‘outputs’ are saved in the results directory for further analysis and interpretation.

# Biof-501 Exploring Patient Groupings in Social and Symptom Problem Index (SSPI) Rankings

## Repository Contents
### Directories
- `bin`: Contains all the python scripts that are used in the pipeline
- `input`: Contains the input data for the pipeline

### Files
- `Dockerfile`: Contains specifications for a Docker image with some required python packages installed 
- `Makefile`: Contains `make` commands for building the docker image and running the workflow
- `workflow.nf`: The primary pipeline implementation
- `nextflow.config`: Configuration file for Nextflow

## Background
Schizophrenia is a psychiatric disorder characterized by positive symptoms, negative symptoms, and cognitive impairments. [1] Positive symptoms consist of delusions, hallucinations, and disorganized speech and behavior. [1] Negative symptoms may consist of non-verbal expression, low expression, etc. [2] To measure these symptoms, typically a Signs and Symptoms of Psychotic Illness (SSPI) rating scale is used. The SSPI is a 20-item rating scale design to measure the severity of the major symptoms in psychotic disorders. [3] The scores range from 0 (absent) to 4 (severe). The first 19 items measure the major signs and symptoms while item 20 assesses insight. [4]

<img width="991" alt="Screenshot 2024-12-04 at 11 46 10 PM" src="https://github.com/user-attachments/assets/25479c7f-21d5-4bb8-ba96-043ab637e8fd">

The purpose of clustering SSPI data is to uncover meaningful patterns and subgroups in individuals with schizophrenia. Firstly, it provides valuable insights into symptom heterogeneity. By grouping patients with similar symptom profiles, clustering has the potential to uncover distinct phenotypes, such as those with severe delusions or cognitive impairments. Secondly, these clusters have the potential to inform more personalized treatment strategies by identifying targeted interventions that are tailored to specific symptoms. For example Cognitive Behavioral Therapy (CBT) can be recommended to patients who suffer more from delusions and Cognitive Remediation Therapy (CRT) can be recommended to those who have more cognitive impairments. Finally, clustering helps researchers better understand and categorize patients, making it easier to explore how their symptoms relate to specific research findings. This deeper understanding of schizophrenia can lead to more effective studies and treatments.

In this pipeline, we are using SSPI from 70 participants with schizophrenia in order to gain insights into symptom patterns, and identify distinct subgroups. This dataset is from a published 2022 study [3]. Patients with psychosis were recruited through Vancouver Coastal Health mental health teams, psychiatric hospitals, and community health agencies [3].

A pipeline is crucial for this analysis because it ensures the systematic, efficient, and reproducible processing of SSPI data. The purpose of this pipeline is really to provide a tool for data analysis and visualization of SSPI rankings that are typically collected in schizophrenia-based studies . First we will need to load the data. As the data may require preprocessing, we have a dedicated step for this task. Next a principal component analysis is performed. Finally the pipeline clusters the patients based on their SSPI rankings.

![Untitled presentation (2)](https://github.com/user-attachments/assets/ee7d05d1-4d7b-489d-b8eb-d9f4e2680331)

## Usage

### Prerequisites

- Docker>=27.3.1 - [Install Here](https://docs.docker.com/desktop/)
- Python>=3.10 - [Install Here](https://www.python.org/downloads/)
- Nextflow>=24.10.1 - [Install Here](https://www.nextflow.io/docs/latest/install.html)

### Running the Workflow

1. Clone the project: 
   ```
   git clone https://github.com/ericayzeng/Biof-501.git
   ```
2. Make sure the `/input` folder contains `Fouladirad_FISH_SSPI.csv`.
3. Ensure that the Docker daemon is running
4. Run 
   ```
   make build-image clean run
   ```
7. On subsequent runs, run 
   ```
   make clean run
   ```

## Input Data
This analysis uses SSPI ranking data from 70 participants with schizophrenia obtained from a [2022 pulished study](https://pubmed.ncbi.nlm.nih.gov/35405574/). The data is in a csv file and is automatically downloaded during the `git clone` process and saved in the `input` folder. 

## Output Data
Results will be published in the `output` directory. The `output` directory will contain the intermediate datasets, and final outputs. The desired outputs for this project are as follows:
- `preprocessed_Fouladirad_FISH_SSPI.csv`
  - A CSV of cleaned and standardized SSPI data ready for analysis
- `pca_results.csv`
  - A CSV of PCA-transformed data with principal components and participant IDs
- `kmeans_results.csv`
  - A CSV mapping participant IDs to their K-means cluster assignments
- `kmeans_3d.png` 
  - A 3D scatter plot showing K-means clusters in PCA-reduced space
- `kmeans_sspi_heatmap.png`
  - A heatmap showing the average SSPI scores for each cluster
- `kmeans.png`
  - An intertia plot for determining the optimal number of clusters 

### PCA
In the PCA step of the pipeline, Principal Component Analysis (PCA) is applied to the preprocessed SSPI dataset to reduce dimensionality and identify patterns in the data. Three principal components are generated, capturing the key variability in symptom rankings while preserving essential information and enabling a graph to be outputted. The output includes a CSV file containing the transformed data with components labeled `PC1`, `PC2`, and `PC3`, along with subject IDs for reference. These results are saved in the specified ‘output’ directory and serve as a foundation for further visualization or clustering analysis.

### Clustering
In the clustering step of the pipeline, K-means clustering is applied to the PCA-transformed SSPI dataset to group patients based on their symptom profiles. An optimal number of clusters is determined by analyzing the inertia across a range of cluster values, with the final clustering performed using 6 clusters. The output includes a CSV file mapping patient IDs to their respective cluster assignments. Additionally, the results are visualized through a 3D scatter plot of the clusters based on the principal components and a heatmap showing the centroids of each cluster across SSPI indices. These `outputs` are saved in the results directory for further analysis and interpretation.

![kmeans_3d](https://github.com/user-attachments/assets/54fdcd11-8f31-442c-aefa-79601ddf84d4)
![kmeans_sspi_heatmap](https://github.com/user-attachments/assets/1b3f4287-23b8-4050-aaff-9a03eb87ce81)
![kmeans](https://github.com/user-attachments/assets/178c7f73-c280-45c0-9ef5-d3e3944bc0e6)

## Container
In the pipeline, a custom Docker image is built on-demand using `make build-image` to run each step of the pipeline (each step uses the same image). The image uses the `python:3.10` image as a base, and additionally installs the packages specified in `requirements.txt`. The implementation for this image can be observed in the `Dockerfile`.

## References
1. Rahman T, Lauriello J. Schizophrenia: An Overview. Focus (Am Psychiatr Publ). 2016;14(3):300-307. doi:10.1176/appi.focus.20160006
2. Kaneko K. Negative Symptoms and Cognitive Impairments in Schizophrenia: Two Key Symptoms Negatively Influencing Social Functioning. Yonago Acta Med. 2018;61(2):91-102. doi:10.33160/yam.2018.06.001
3. Fouladirad S, Chen LV, Roes M, et al. Functional brain networks underlying probabilistic reasoning and delusions in schizophrenia. Psychiatry Res Neuroimaging. 2022;323:111472. doi:10.1016/j.pscychresns.2022.111472
4. Liddle PF, Ngan ETC, Duffield G, Kho K, Warren AJ. Signs and Symptoms of Psychotic Illness (SSPI): A rating scale. British Journal of Psychiatry. 2002;180(1):45-50. doi:10.1192/bjp.180.1.45

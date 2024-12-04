#!/usr/bin/env nextflow

/*
This file contains the implementation of the workflow 
for SSPI analysis
*/

// This channel reads data from the input directory
params.reads = Channel.fromPath("$projectDir/input/*.csv")
// This specifies an output directory
params.outputDir = "output"

// This process preprocesses the input data
process PREPROCESS {
    publishDir params.outputDir, mode:'copy'

    input:
    path sample
    
    output:
    path "preprocessed_${sample}"

    script:
    """
    python3 $projectDir/bin/preprocess.py ${sample} "preprocessed_${sample}"
    """
}

// This process performs PCA on the preprocessed data
process PCA {
    publishDir params.outputDir, mode:'copy'

    input:
    path data
    
    output:
    path "pca_results.csv"

    script:
    """
    python3 $projectDir/bin/pca.py ${data} "pca_results.csv"
    """
}

// This process performs K-means clustering on the PCA results
process KMEANS {
    publishDir params.outputDir, mode:'copy'

    input:
    path pca
    path preprocessed
    
    output:
    path "kmeans_results.csv"
    path "kmeans_3d.png"
    path "kmeans_sspi_heatmap.png"
    path "kmeans.png"

    script:
    """
    python3 $projectDir/bin/k_means.py ${pca} ${preprocessed} "kmeans_results.csv"
    """
}

workflow {
    log.info """
    ======================================
                ┏┓┏┓┏┓┳        
                ┗┓┗┓┃┃┃        
                ┗┛┗┛┣┛┻        
                ┏┓┳┓┏┓┓ ┓┏┏┓┳┏┓
                ┣┫┃┃┣┫┃ ┗┫┗┓┃┗┓
                ┛┗┛┗┛┗┗┛┗┛┗┛┻┗┛
    ======================================
    """
    .stripIndent()

    // Step 1: preprocess data
    preprocess_ch = PREPROCESS(params.reads)
    // Step 2: PCA analysis
    pca_ch = PCA(preprocess_ch)
    // Step 3: K-means clustering
    KMEANS(pca_ch, preprocess_ch)
}
#!/usr/bin/env nextflow

// inputs
reads = Channel.fromPath("$projectDir/input/*.csv")
params.outputDir = "output"

log.info """\
    S S P I _ A N A L Y S I S _ W O R K F L O W
    ============================================
    reads        : ${reads}
    outdir       : ${params.outputDir}
    """
    .stripIndent()

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
    preprocess_ch = PREPROCESS(reads)
    pca_ch = PCA(preprocess_ch)
    kmeans_ch = KMEANS(pca_ch, preprocess_ch)
}
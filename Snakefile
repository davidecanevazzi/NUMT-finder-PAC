################################################################################

############################### NUMTs-finder ##################################

###############################################################################



# import modules
import numpy as np

import pandas as pd

import os

import sys

import subprocess

chrM= "'chrM'"



rule fasta:
    output:
    	"data/sample.fasta"
    shell:
    	"seqtk seq -a data/FAN51167_1_0.fastq > {output}"

rule minimap_mit:
    input:
    	"data/sample.fasta"	
    output:
        "data/mit.paf"
    shell:
        "minimap2 -t 24 -z 600,200 -x map-ont data/mit_reference.fasta data/sample.fasta > {output}"

rule select_chrM:
    input:
        "data/mit.paf"
    output:
        "data/mit_reads.txt"
    shell:
        "cut -f1 data/mit.paf > {output}"
	
rule extract_reads:
    input:
        "data/mit_reads.txt"
    output:
        "reads.fasta"
    shell:
        "seqtk subseq data/sample.fasta data/mit_reads.txt > {output}"
        
rule kmers:
    input:
        "reads.fasta"
    output:
        "data/k_mers.fasta"
    shell:
        "python splt_kmers.py > {output}"
        
        
rule minimap_tot:
    input:
    	"data/k_mers.fasta"	
    output:
        "data/aln_pre.paf"
    shell:
        "minimap2 -t 24 -z 600,200 -x map-ont data/GRCh38.primary_assembly.genome.fa data/k_mers.fasta > {output}"
    
rule filt:
    input:
    	"data/aln_pre.paf"	
    output:
        "data/aln.paf"
    shell:
    	"awk '$12 >= 30' {input} > {output}"
    	    
rule greps_mit:
    input:
    	"data/aln.paf"	
    output:
        "chrM.paf"
    shell:
    	" grep {chrM} data/aln.paf > {output}"
        
rule greps_nuc:
    input:
    	"data/aln.paf"	
    output:
        "nuc.paf"
    shell:
    	"grep -v {chrM} data/aln.paf > {output}"
        
rule detect_NUMTs:
    input:
    	mit="chrM.paf",nuc="nuc.paf"
    output:
        "NUMTs.txt"
    shell:
        "python detect_NUMTs.py > {output}"

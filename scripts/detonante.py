#!/usr/bin/python -tt
# Running of DETONATE for analysis of assemblies
# From: http://deweylab.biostat.wisc.edu/detonate/vignette.html

# Import OS to run external programs
import os
import glob

assem_dir = "/media/transcriptome/assembly"
fastq_file = "/media/transcriptome/qc/Ha_Vib.fastq"

print "Scanning directory %s..." % (assem_dir)
# Pull in files
fasta_files = sorted(glob.glob(assem_dir + "/*.fasta"))

trim = len(list(fasta_files))

for files in range(trim):
	sample_name = os.path.splitext(os.path.basename(fasta_files[files]))[0]
	print "Analyzing %s..." % (sample_name)
	#print fasta_files[files]
	os.system("/home/chris/bin/detonate-1.9/rsem-eval/rsem-eval-calculate-score --bowtie2 %s %s %s 51 -p 4" % (fastq_file, fasta_files[files], sample_name))

#!/usr/bin/python -tt
# Uses fastqc to examine quality of raw and trimmed data
# Website: http://www.bioinformatics.babraham.ac.uk/projects/fastqc/
# Change of directory can be used to run on different files

# Import OS features to run external programs
import os
import glob

# Setup directories to the data
fastq_trimmed = "/media/transcriptome/qc/"
fastq_toutput = "/media/transcriptome/reports/"

#print "Raw Directory: %s\n" % (fastq_raw)
print "Trimmed Directory: %s\n" % (fastq_trimmed)
print "Scanning Raw Directory..."

# Pull file names from raw
#fastq_rfiles = glob.glob1(fastq_raw, "*.fastq")
fastq_tfiles = sorted(glob.glob1(fastq_trimmed, "*.fastq"))
#print fastq_tfiles

trim = len(list(fastq_tfiles))
for files in range(trim):
	#print fastq_tfiles[files]

	fastqc_trun = fastq_trimmed + fastq_tfiles[files]
	
	# Run fastqc
	os.system("~/bin/FastQC/fastqc -o %s %s" % (fastq_toutput, fastqc_trun))

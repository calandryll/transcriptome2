#!/usr/bin/python -tt
# Run Trimmomatic to remove Illumina adapter sequences
# Update on: 031615
# Updated for new system analysis
# Going to use default TruSeq3 adapters included with trimmomatic
# From: http://www.usadellab.org/cms/?page=trimmomatic

# Import OS to run external programs
import os
import glob

orig_dir = "/media/transcriptome/originals"
qc_outdir = "/media/transcriptome/qc"
#adapters = "/media/transcriptome/fasta/Illumina_truseq_adapter.fasta"
logfile = "/media/transcriptome/qc/log.txt"

print "Scanning directory %s..." % (orig_dir)
# Pull in files
fastq_files = sorted(glob.glob(orig_dir + "/*.fastq"))

trim = len(list(fastq_files))

for files in range(trim):
	sample_name = os.path.splitext(os.path.basename(fastq_files[files]))[0]
	print "Analyzing %s..." % (sample_name)
	#samdir = orig_dir + "/" + fastq_files[files]
	outdir = qc_outdir + "/" + sample_name + "_trimmed.fastq"
	# Remove Illumina Sequences and then keep any sequence that is longer than 35 bp
	os.system("java -jar /home/chris/bin/trimmomatic/trimmomatic-0.33.jar SE %s %s ILLUMINACLIP:/home/chris/bin/trimmomatic/adapters/TruSeq3-SE.fa:2:30:10 MINLEN:35 >> %s" % (fastq_files[files], outdir, logfile))


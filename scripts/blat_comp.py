#!/usr/bin/python -tt
# Running of DETONATE for analysis of assemblies
# From: http://deweylab.biostat.wisc.edu/detonate/vignette.html

# Import OS to run external programs
import os
import glob

# Set the file that will be blated against
dbase_fasta = "/media/transcriptome/assembly/Trinity_rsem.fasta"
assem_dir = "/media/transcriptome/assembly"

print "Scanning directory %s..." % (assem_dir)
# Pull in files
fasta_files = sorted(glob.glob(assem_dir + "/*.fasta"))

trim = len(list(fasta_files))

for files in range(trim):
	sample_name = os.path.splitext(os.path.basename(fasta_files[files]))[0]
	print "Analyzing %s..." % (sample_name)
	sample_out = sample_name + ".psl"
	#print fasta_files[files]
	os.system("/home/chris/bin/blat %s %s %s -t=dna -q=dna -out=blast9" % (dbase_fasta, fasta_files[files], sample_out))

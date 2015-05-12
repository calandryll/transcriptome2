#!/usr/bin/python -tt
# Search for Heterosigma 18S Primers and pull those sequences out

# Allow to open fasta files
from Bio import SeqIO
# Read arguments from the commandline
import numpy
# Import OS to run external programs
import os
import glob

assem_dir = "/media/transcriptome/assembly/fasta"

print "Scanning directory %s..." % (assem_dir)
# Pull in files
assem_files = sorted(glob.glob(assem_dir + "/*.fasta"))
output_handle = open("sequences.txt", "w")
trim = len(list(assem_files))
#fasta_dict = SeqIO.parse(fasta_handle, 'fasta')
f_seq = "CTAAATAGTGTCGGTAATGCTTCT"
r_seq = "GGCAAGTCACAATAAAGTTCCAT"

for files in range(trim):
	sample_name2 = os.path.splitext(os.path.basename(assem_files[files]))[0]
	sample_name = assem_files[files]
	# Open the file
	fasta_dict = SeqIO.parse(sample_name, 'fasta')
	output_handle.write("File: %s" % sample_name2 + "\n")

	for records in fasta_dict:
		# print ">" + records.id
		# print records.seq
		if f_seq in records.seq:
			SeqIO.write(records, output_handle, "fasta")
		if r_seq in records.seq:
			SeqIO.write(records, output_handle, "fasta")
output_handle.close()
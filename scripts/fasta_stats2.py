#!/usr/bin/python -tt
# Calculate N50, Max Contig length and Mean Contig Length

# Allow to open fasta files
from Bio import SeqIO
# Read arguments from the commandline
import numpy
# Import OS to run external programs
import os
import glob

assem_dir = "/media/transcriptome/assembly"

print "Scanning directory %s..." % (assem_dir)
# Pull in files
assem_files = sorted(glob.glob(assem_dir + "/*.fasta"))
output_handle = open("stats.txt", "w")
trim = len(list(assem_files))

for files in range(trim):
	seqlength = []
	unique = []
	n50 = []
	avg = []
	blarg = []

	sample_name2 = os.path.splitext(os.path.basename(assem_files[files]))[0]
	sample_name = assem_files[files]
	print "Analyzing %s..." % (sample_name2)
	# Open the file
	fasta_dict = SeqIO.parse(sample_name, 'fasta')

	for records in fasta_dict:
		bp = len(records.seq)
		seqlength.append(bp)

	seqlength = sorted(seqlength)

	for entry in seqlength:
		if not entry in unique:
			unique.append(entry)

	for entry in unique:
		multiplier = seqlength.count(entry) * entry
		for i in range(multiplier):
			n50.append(entry)

	index = len(n50)/2
	output_handle.write("File: %s" % sample_name2 + "\n")
	if index % 2==0:
		first = n50[index - 1]
		second = n50[index]
		avg.append(first)
		avg.append(second)
		n50 = numpy.mean(avg)
		output_handle.write("N50: %s" % n50 + "\n")
	else:
		output_handle.write("N50: %s" % n50[index - 1] + "\n")

	# Write to file
	output_handle.write("Maximum contig length: %s" % seqlength[-1] + "\n")
	output_handle.write("Median contig length: %s" % numpy.median(seqlength) + "\n")
	output_handle.write("Mean contig length: %s" % numpy.mean(seqlength) + "\n")
	output_handle.write("Standard deviation contig length: %s" % numpy.std(seqlength) + "\n")
	output_handle.write("# of contigs: %s" % len(seqlength) + "\n\n")

blarg = seqlength>=1000
output_handle.close()

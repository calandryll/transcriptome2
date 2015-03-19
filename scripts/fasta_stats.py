#!/usr/bin/python -tt
# Calculate N50, Max Contig length and Mean Contig Length

# Allow to open fasta files
from Bio import SeqIO
# Read arguments from the commandline
import argparse
import numpy

# Read and parse the arguments from the command line
parser =  argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="version", version='Version 0.1')
parser.add_argument("filename", help="location of FASTA file")
args = parser.parse_args()

# Open the file
fasta_handle = open(args.filename, "rU")
output_handle = open(args.filename + ".txt", "w")
fasta_dict = SeqIO.parse(fasta_handle, 'fasta')

seqlength = []
unique = []
n50 = []
avg = []
blarg = []

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

if index % 2==0:
	first = n50[index - 1]
	second = n50[index]
	avg.append(first)
	avg.append(second)
	n50 = numpy.mean(avg)
	output_handle.write("N50: %s" % n50 + "\n")
else:
	output_handle.write("N50: %s" % n50[index - 1] + "\n")

blarg = seqlength>=1000
output_handle.write("Maximum contig length: %s" % seqlength[-1] + "\n")
output_handle.write("Median contig length: %s" % numpy.median(seqlength) + "\n")
output_handle.write("Mean contig length: %s" % numpy.mean(seqlength) + "\n")
output_handle.write("# of contigs: %s" % len(seqlength) + "\n")
output_handle.close()
fasta_handle.close()

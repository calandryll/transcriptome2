#!/usr/bin/python -tt
# Remove sequences under X number

# Allow to open fasta files
from Bio import SeqIO
# Read arguments from the commandline
import argparse
import os

# Read and parse the arguments from the command line
parser =  argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="version", version='Version 0.1')
parser.add_argument("filename", help="location of FASTA file")
parser.add_argument("--min_seq", help="Minimum sequence length to be kept (Default is 200 bp)", type = int, default = 200)
args = parser.parse_args()

# Open the file
cleaned_name = os.path.splitext(os.path.basename(args.filename))[0]
output_handle = open(cleaned_name + "_cleaned.fasta", "w")
min_seq = args.min_seq

sequences = []

print "Analyzing %s..." % (cleaned_name)

for i in SeqIO.parse(args.filename, "fasta"):
    sequence=str(i.seq).upper()
    if len(sequence) >= min_seq:
        SeqIO.write(i, output_handle, "fasta")

output_handle.close()
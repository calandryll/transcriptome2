#!/usr/bin/python -tt
# Automated BLAST search of a FASTA file. Search defaults to blastx (Protein) search,
# blast type, database, e-value threshold and number of hits can be changed with 
# commandline inputs.
# Any inputs with - or -- are optional and will default to certain values.
# Blast will be done locally for quicker responses
# Written by: Christopher R. Main, University of Delaware
# Last Updated: 09/26/13

# Versions:
#	0.1 - Open Cluster file and begin searching internet blast
#	0.2 - Search and send output to screen of top result
#	0.3 - Output BLAST results with GI, Length, E-Value, Query Start, Subject Start, Score and Bits
#	0.4 - Setup of for loop to run multiple queries, and output to separate files
#	0.5 - Append data to the file with added sequence name to first column
#	0.6 - Change way of doing inputs
#	Future versions:
#	0.7 - Write for local database search, for use on BioHen

# Allow manipulating of FASTA file
from Bio import SeqIO
# Import OS to run external programs
import os
import glob

assem_dir = "/media/transcriptome/assembly/fasta"
blast_db = "/media/transcriptome/assembly/fasta/trinity_all.fasta"

assem_files = sorted(glob.glob(assem_dir + "/*.fasta"))
trim = len(list(assem_files))

print "Scanning directory %s..." % (assem_dir)

# Run through a blast search for all of the files in the directory
for files in range(trim):
	sample_name2 = os.path.splitext(os.path.basename(assem_files[files]))[0]
	sample_name = assem_files[files]
	out_file = sample_name2 + ".txt"

	print "Analyzing %s..." % (sample_name2)

	# Perform the blast search
	os.system("blastn -db %s -out %s -query %s -outfmt 6 -evalue 1e-20 -max_target_seqs 1 -num_threads 4" % (blast_db, out_file, sample_name))

	# Write the 
	os.system("/home/chris/bin/trinityrnaseq/util/analyze_blastPlus_topHit_coverage.pl %s %s %s" % (out_file, sample_name, blast_db))


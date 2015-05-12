#!/usr/bin/python -tt
# Run all of the steps in a single script
# Next revision will include interactive steps for input of data (perhaps)

# Import OS features to run external programs
import os
import glob
import datetime

qc_dir = "/media/transcriptome/qc"
align_dir = "/media/transcriptome/analysis/align"
reference = "/media/transcriptome/reference/H_akashiwo"
assem_dir = "/media/transcriptome/analysis/assemble"
merge_dir = "/media/transcriptome/analysis/merged"
merged = "/media/transcriptome/analysis/merged/merged.gtf"
diff_dir = "/media/transcriptome/analysis/diff/"
ha_gff = reference + ".gff3"

def ref_align():
	# Directories for input and output
	print "Beginning tophat mapping..."
	#print "Raw Directory: %s\n" % (fastq_raw)
	print "Directory: %s\n" % (qc_dir)
	#print "Using %s as a reference..." % (ha_gff)
	print "Scanning Directory..."

	# Pull files from directory
	fastq_files = sorted(glob.glob(qc_dir + "/*.fastq"))

	trim = len(list(fastq_files))
	for files in range(trim):
		#print fastq_files[files]
		localtime = datetime.datetime.now() # Timestap of start
		print "Start time of analysis: %s" % (localtime)
		sample_name = os.path.splitext(os.path.basename(fastq_files[files]))[0]
		print "Analyzing %s..." % (sample_name)
		#print sample_name
		samdir = align_dir + "/" + sample_name
		#print samdir
		#print fastq_files[files]	

		# Create directory for output
		os.system("mkdir %s" % (samdir))

		# run tophat using H_akashiwo index
		# -p 4 threads
		# Segment length changed to half of fragments, to appease warning
		# 090814 - removed --segment-length 19 since reads are on avg now 51 bp
		# 090814 - added logfile output
		os.system("~/bin/tophat/tophat -p 4 -o %s %s %s" % (samdir, reference, fastq_files[files]))

	# Copy accepted hits for DE analysis
	print "Copying accepted_hits.bam to proper directories..."
	os.system("cp %s/Control_2/accepted_hits.bam %s/controls/control_2.bam" % (align_dir, align_dir))
	os.system("cp %s/Control_3/accepted_hits.bam %s/controls/control_3.bam" % (align_dir, align_dir))
	os.system("cp %s/Control_4/accepted_hits.bam %s/controls/control_4.bam" % (align_dir, align_dir))
	os.system("cp %s/Treat_1/accepted_hits.bam %s/treat/treat_1.bam" % (align_dir, align_dir))
	os.system("cp %s/Treat_2/accepted_hits.bam %s/treat/treat_2.bam" % (align_dir, align_dir))
	os.system("cp %s/Treat_3/accepted_hits.bam %s/treat/treat_3.bam" % (align_dir, align_dir))

	
def assemble():
	#print "Raw Directory: %s\n" % (fastq_raw)
	print "Beginning cufflinks assembly..."
	print "Directory: %s\n" % (align_dir)
	print "Scanning Directory..."

	# Pull files from directory
	fastq_files = sorted(glob.glob(align_dir + "/*/accepted_hits.bam"))
	fastq_dir = sorted(glob.glob(align_dir + "/*"))

	trim = len(list(fastq_files))
	for files in range(trim):
		#print fastq_files[files]
		localtime = datetime.datetime.now() # Timestap of start
		print "Start time of analysis: %s" % (localtime)
		sample_name = os.path.splitext(os.path.basename(fastq_files[files]))[0]
		dir_name = os.path.splitext(os.path.basename(fastq_dir[files]))[0]
		print "Analyzing %s..." % (dir_name)
		
		samdir = assem_dir + "/" + dir_name
		#print samdir
		
		# Create directory for output
		os.system("mkdir %s" % (samdir))

		# Run tophat using H_akashiwo index
		# -p 4 threads
		# try -G
		os.system("~/bin/cufflinks/cufflinks -p 4 -o %s %s" % (samdir, fastq_files[files]))

def merge():
	localtime = datetime.datetime.now() # Timestap of start
	print "Start time of analysis: %s" % (localtime)
	os.system("~/bin/cufflinks/cuffmerge -o %s %s/gtf.txt" % (merge_dir, assem_dir))

# def quant():
# 	localtime = datetime.datetime.now() # Timestap of start
# 	print "Start time of analysis: %s" % (localtime)


# 	# Run cuffquant.  This produces a normalized file for each sample
# 	os.system("~/bin/cufflinks-2.2.1/cuffquant -p 4")

def diff():
	localtime = datetime.datetime.now() # Timestap of start
	print "Start time of analysis: %s" % (localtime)
	control_lane = align_dir + "/controls"
	treat_lane = align_dir + "/treat"

	#print control_lane
	#print treat_lane
	os.system("~/bin/cufflinks/cuffdiff --max-bundle-frags 2000000 -p 4 -L Control,Vibrio -o %s %s %s/control_2.bam,%s/control_3.bam,%s/control_4.bam %s/treat_1.bam,%s/treat_2.bam,%s/treat_3.bam" % (diff_dir, merged, control_lane, control_lane, control_lane, treat_lane, treat_lane, treat_lane))
	# Hey idiot double check that shit!
	# Removed treat_4.bam - maybe a bit off
	# HIDATA means too many fragments, will add --max-bundle-frags 2000000

def cummeRbund():
	os.system("Rscript fastq/cummerbund_analysis.r")

ref_align()
assemble()
merge()
diff()
#cummeRbund()

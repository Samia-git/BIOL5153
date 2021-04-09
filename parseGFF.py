print("Hello world")
#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqI0

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumenrParser(description='this script will parse a GFF file and extract each feature from the genome') 

#add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help= 'name of the Fasta file')

#parse the arguments
args = parser.parse_args()

# read in FASTA
genome = SeqI0.read(args.fasta, 'fasta')
print(genome.id)
print(genome.seq)

# open and read in GFF file
with open(args.gff, 'r') as gff_in:

     #create a csv object
     reader = csv.reader(gff_in, delimiter='\t')

     #loop over all the lines in our reader object (i.e., pars file)
     for line in reader:
         start = line[3]
         end   = line[4]
         strand= line[6]
         #print(start)
         #print(line[3], line[4])


         #extract the sequence
         print(len(genome.seq))

   #parse the GFF file
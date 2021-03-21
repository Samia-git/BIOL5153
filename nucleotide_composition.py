#! /usr/bin/env python3

#set the name of input DNA sequence file
filename = 'nad4lsequencefile.txt'

# open the input file, assign to file handle called 'infile'
infile = open(filename, 'r')

#print(infile) 

# read the file
dna_seq = infile.read()

#print the dna_seq
print(dna_seq)

#close the file
infile.close()

#Frequency
dna_A = dna_seq.count('A')
dna_C = dna_seq.count('C')
dna_G = dna_seq.count('G')
dna_T = dna_seq.count('T')

#Ratio
dna_ratio_A = dna_A / len(dna_seq)
dna_ratio_C = dna_C / len(dna_seq)
dna_ratio_G = dna_G / len(dna_seq)
dna_ratio_T = dna_T / len(dna_seq)
GCcontent = dna_ratio_G + dna_ratio_C

#Printing output
print("Frequency of A: "+"{:.3f}".format(dna_ratio_A));
print("Frequency of C: "+"{:.3f}".format(dna_ratio_C));
print("Frequency of G: "+"{:.3f}".format(dna_ratio_G));
print("Frequency of T: "+"{:.3f}".format(dna_ratio_T));
print("G and C content: ", "%.3f" % GCcontent)

#Total Ratio
frequency = dna_ratio_A + dna_ratio_G + dna_ratio_T + dna_ratio_C
print(frequency)

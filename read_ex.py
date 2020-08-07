#!/usr/bin/python
import sys
from Bio import SeqIO

print('\nUsage: read_ex.py File.fasta List.txt\n')


# open fasta and list of reads
try:
	fasta = sys.argv[1]
except:
	fasta = input('Reads FASTA file: ')  
	
try:
	lista = sys.argv[2]
except:
	lista = input('List name file: ')

#Opening FASTA and LIST
data = SeqIO.parse(open(fasta), "fasta")
l_op = open(lista, 'r').readlines() 

#creating lists
fa_head   = []
fa_values =	[]
read_list = []

#Appendind data in lists
for x in data:
	fa_head.append(str(x.id))
	fa_values.append(str(x.seq))
for i in l_op:
	read_list.append(i.replace("\n", ""))

for reads in read_list:
	count = 0
	outp = open(reads.replace("/", "-") + '.fasta', 'w')
	for i in fa_head:
		if i != reads:
			count += 1
		elif i == reads:
			count = count
			outp.write(fa_head[count] + '\n' + fa_values[count] + '\n')

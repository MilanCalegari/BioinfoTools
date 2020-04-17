from Bio import SeqIO
import sys

try:
	file = sys.argv[1]
except:
	file = input("Introduce FASTA file: ") 

data = SeqIO.parse(open(file), "fasta")
outp = open(file.replace('.fasta', '.bed'), 'w')

seq_dict = {}

for i in data:
	seq_dict[str(i.id)] = str(i.seq)


for x,y in seq_dict.items():
	outp.write('{}\t0\t{}\n' .format(x, len(y)))

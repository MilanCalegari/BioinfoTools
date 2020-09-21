#!/usr/bin/env python3

import sys
from subprocess import call

def how_many_cats(count,number):   #how many times a need to write the fasta file to get x number of reads
	if int(number) >= count:
		value = int(number)/int(count/2)
		return round(value) + 1
	else:
		return 1

try:
	lista = sys.argv[1]
except:
	lista = input('insert lista with both sel.fq files: ')

try:
	read_numbers = sys.argv[2]
except:
	read_numbers = input('insert the ~number of reads of output file: ')

lib = open(lista,'r').readlines()

fwd = lib[0].replace('\n','')
rev = lib[-1].replace('\n','')

merged_fq = fwd.split('1')[0]+'12.fq'
merged_fasta = merged_fq.replace('fq','fasta')

call('cat %s %s > %s'%(fwd,rev,merged_fq),shell=True)
call('seqtk seq -a %s > %s'%(merged_fq, merged_fasta), shell=True)
call('rm '+ merged_fq, shell=True)

fasta_merged = open(merged_fasta,'r').readlines()
count = (len(open(merged_fasta).readlines()))
num = how_many_cats(count,read_numbers)
outp = open(fwd.split('1')[0]+'12_final.fasta','w')
c = 0

while c < num:
	for line in fasta_merged:
		outp.write(line)
	c += 1

call('rm ' + merged_fasta, shell=True)
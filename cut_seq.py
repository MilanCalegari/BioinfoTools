#!/usr/local/bin/python

import sys, os
from subprocess import call

try:
	lib = sys.argv[1]
except:
	lib = input('Insert a list of fastq.gz files: ')

try:
	sample = sys.argv[2]
except:
	sample = input('Insert the number of sub-samples: ')

try:
	size = sys.argv[3]
except:
	size = input('Insert the size of reads: ')


def rename(seq):
	try:
		return seq.replace('.fastq.gz','')
	except:
		return seq.replace('.fq.gz','')



lib = open(lib,	'r').readlines()
fwd = lib[0].replace('\n','')
rev = lib[-1].replace('\n','')

try:
	sample_list = []
	sample_list = sample.split(',')
except:
	sample_list = sample

try:
	size_list = []
	size_list = size.split(',')
except:
	size_list = size


for j in sample_list:
	outp1 = rename(fwd)+'_'+j+'.fastq'
	outp2 = rename(rev)+'_'+j+'.fastq'
	call('seqtk sample -s100 %s %s > %s'%(fwd,j,outp1),shell=True)
	call('seqtk sample -s100 %s %s > %s'%(rev,j,outp2),shell=True)
	for i in size_list:
		final1 = rename(fwd)+'_'+j+'_'+i+'.fastq'
		final2 = rename(rev)+'_'+j+'_'+i+'.fastq'
		call('TrimmomaticPE -phred33 %s %s %s lixo1 %s lixo2 ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:100 CROP:%s'%(outp1,outp2,final1,final2,i),shell=True)
	os.remove(outp1)
	os.remove(outp2)

call('rm *lixo*',shell=True)
print("\nIt's Done!!\n")
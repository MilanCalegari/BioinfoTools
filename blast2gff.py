#/usr/local/bin/python3

import sys

try:
	inp = sys.argv[1]
except:
	inp = input('insert blast outp: ')

data = open(inp, 'r').readlines()

try:
	name = sys.argv[2]
except:
	name = input('insert outp name: ')

outp = open(name,'w')

for i in data:
	s = i.split()
	if s[8] < s[9]:
		outp.write('%s	manual	%s	%s	%s	.	+	.	' %(s[1],s[0],s[8],s[9]))
	else:
		outp.write('%s	manual	%s	%s	%s	.	-	.	' %(s[1],s[0],s[9],s[8]))

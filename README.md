# BioinfoTools

fasta2bed.py  -> Convert a fasta file in a anntotation file (.bed)  
usage: fasta2bed.py [fastaFile]  
  
reads_ex.py    -> Extracts the reads (sequences) from a fasta file.  
usage: reads_ex.py [fileFasta] [readsId.txt]

cut_seq.py	-> Make a subsample of x and cut the reads in length y.  
usage: cut_seq.py [x1,xn] [y1,yn] 

blast2gff.py	-> Make a gff file from Blast output (outfmt = 6).  
usage: blast2gff.py [blast output file] [output name]  

selfq2fasta.py	-> Merge to files *sel.fq into one fasta file with ~x reads.  
usege: selfq2fasta.py [list of sel.fq files] [aproximate number of reads]

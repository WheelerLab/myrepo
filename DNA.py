#!/usr/bin/python

seq = open('rosalind_dna.txt','r').read()

a = seq.count("A")
c = seq.count("C")
g = seq.count("G")
t = seq.count("T")
 
print a, c, g, t



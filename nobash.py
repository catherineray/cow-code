"""
The challenge: without using a bash script, write a one liner that reads through all the lines in a file, sorts them and printed these sorted lines to stdout. Do so in under a minute without using the internet.
"""

One liners:
#print '\n'.join(sorted([line.strip() for line in open("file.txt")]))
#import sys; print '\n'.join(sorted([line.strip() for line in open(sys.argv[1])]))

import sys
try:
 with open(sys.argv[1]) as f:
  for line in f:
   print '\n'.join(sorted(line.strip())) 
except IOError:
 print "File does not exist."
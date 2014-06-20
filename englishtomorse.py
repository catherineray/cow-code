#!usr/bin/python
#Catherine Ray

"""
morse.py {string} [{string} ... ]:
 Translates string of english letters and spaces to morse code.
"""

import string
import sys

if len(sys.argv)>=2:
 if sys.argv[1].isalpha():
  text = ''.join(sys.argv[1:]).lower()
  morse = ["01","1000","1010","100","0", "0010", "110", "0000", "00", "0111", "101", "0100", "11", "10", "111", "0110", "1101", "010", "000", "1", "001", "0001", "011", "1001", "1011", "1100"]
  letter = map(chr, range(97, 123))
  LETTER_TO_MORSE = dict(zip(letter, morse))
  morse_out = [LETTER_TO_MORSE[x] for x in text]
  print ' '.join(morse_out).replace("1","-").replace("0",".")
 else:
  "Restrict yourself to the english alphabet."
else: 
 print "Enter a string to translate, friend!"
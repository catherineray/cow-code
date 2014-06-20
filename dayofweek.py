# dayofweek.py
import datetime
from sys import argv
from calendar import day_abbr #import day_name for full name

"""
Counts the amount of hits per weekday, given a file of data corresponding to "year month day amount-of hits"
"""
#starts with a zero counter array (each index corresponds to a weekday, 0:Sunday, 1:Monday, ...)
weekcount = [0]*7 #hits per day
argv = argv[1:] #get rid of script declaration in args

#make sure string has year, month, day, amount-of-hits-that-day
if len(argv) % 4 == 0:
  for c in range(0, len(argv),4):
    #increment slice so we are only looking at one set of (year, month, day, amount-of-hits-that-day) at one time
     if (a.isdigit() for a in argv[0+c:4+c]):
         year, month, day, count = int(argv[0+c]), int(argv[1+c]), int(argv[2+c]), int(argv[3+c]);
         #get index of day that the given date corresponds to
         daynum = int(datetime.date(year, month, day).strftime("%w"))
         #add the amount-of-hits-that-day to the counter
         weekcount[daynum] = weekcount[daynum] + count;

  #display days from most to least popular
  print '\n'.join([day_abbr[(sorted(range(7), key=lambda k: weekcount[k]))[d]] for d in range(7)])
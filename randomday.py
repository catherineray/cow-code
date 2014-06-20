# randomday.py
import random as r

f=[]
for x in xrange(12):
 year = r.choice(range(1997, 2013))
 month = r.choice(range(1, 12))
 day = r.choice(range(1, 28))
 hits = r.choice(range(6666,9999))
 f.extend((year, month, day, hits))

print ' '.join(map(str,f))
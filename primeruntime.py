'''
Catherine Ray
prime_runtime0.py

'Algorithms Unplugged' Demonstration
Program uses algorithms listed in psuedocode from pg.119-127. Each algorithm returns a list of all primes up to some number n.
There are 4 versions of this algorithm; this program computes the average runtimes of each version and prints to stdout.
'''

import math
import time as t

class Runtime():
 def execute(self):
  repeat = 1000 #number of times to repeat runtime calculation
  n = [2**x for x in xrange(6, 21, 7)] #produce list of large numbers to test algorithms
  #n = [2**6, 2**20]
  for v in xrange(1,5):
   method = 'self.prime_number'+str(v) #test each version of the algorithm, version = 1, 2, 3, 4
   print '\n\tVersion ' + str(v), '\nHighest Prime Number Computed : Average Runtime\n'  #find runtime
   [self.runtime(method, number, repeat) for number in n] 
   
  

 def runtime(self, method, n, repeat):
 #function = function to test
 #n = highest prime to compute
 #repeat = number of trials to run
  method = eval(method)
  total = 0 #reset total
  for r in xrange(0, repeat+1): 
   start = t.time() #get start time
   methodrun=method(n) 
   end = t.time() #get end time
  total = total + end-start #add to previously calculated time
  average_time = total/repeat #find average runtime
  print  '2^%d :' %(int(math.log(n)/math.log(2))), average_time
  
 

 def prime_number1(self, n): #version 1, pg. 121
  list = [i for i in xrange(2,n+1)] #write down all numbers between 2 and n in a list
  for i in xrange(2, n+1):
   for k in xrange(2, n+1):
    if i*k in list: list.remove(i*k) #if i*k is in list, remove
    else: pass #if i*k isn't in list, do nothing
  return list


 def prime_number2(self, n): #version 2, pg. 123
  list = [i for i in xrange(2,n+1)] #write down all numbers between 2 and n in a list
  for i in xrange(2, int(math.floor(math.sqrt(n)))+1):
   for k in xrange(2, int(math.floor(n/i))+1):
    if i*k in list: list.remove(i*k) #if i*k is in list, remove
    else: pass #if i*k isn't in list, do nothing
  return list

 def prime_number3(self, n): #version 3, pg. 125
  list = [i for i in xrange(2,n+1)] #write down all numbers  between 2 and n in a list
  for i in xrange(2, int(math.floor(math.sqrt(n)))+1):
   if i in list:
    for k in xrange(2, int(math.floor(n/i))+1):
     if i*k in list: list.remove(i*k) #if i*k is in list, remove
     else: pass #if i*k isn't in list, do nothing
  return list


 def prime_number4(self, n): #final version, pg.127
  list = [i for i in xrange(2,n+1)] #write down all numbers between 2 and n in a list
  for i in xrange(2, int(math.floor(math.sqrt(n)))+1):
   if i in list:
    for k in xrange(int(math.floor(n/i)), i-1, -1):
     if k in list:
      if i*k in list: list.remove(i*k)  #if i*k is in list, remove
      else: pass #if i*k isn't in list, do nothing
  return list

if __name__ == '__main__':
 runtime = Runtime()
 runtime.execute()
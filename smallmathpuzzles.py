x=1234

for n in range(0, x-1):
  if (n*(n+1))/2 > x: 
    tri =n-1
    print x*2-tri 
    break
#sudo apt-get install python-visual
#http://www.rin.io/2013/11/yddc-simple-cubic-lattice.html

from visual import sphere
L = 5
R = 0.3
for i in range(-L,L+1):
 for j in range(-L,L+1):
  for k in range(-L,L+1):
   sphere(pos=[i,j,k],radius=R)
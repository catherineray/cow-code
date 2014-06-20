#type individual brl cell using numkeys
from visual import sphere
R = 0.2 #filled dot radius
r = 0.1 #empty dot radius

#corresponds to numkeys
dotdict = {
'7': [1,3], #dot 1 
'4': [1,2], #dot 2
'1': [1,1], #dot 3
'8': [2,3], #dot 4
'5': [2,2], #dot 5
'2': [2,1] #dot 6
}

fulldot = dotdict.keys()

def draw(dots):
 [sphere(pos=dotdict[dot], radius=r) for dot in fulldot] #create empty dot matrix to represent empty cell
 [sphere(pos=dotdict[dot], radius=R) for dot in dots] #fill appropriate dots

print "Please enter string\n7\t8\n4\t5\n1\t2\n: "
string = raw_input()
if string.isdigit(): draw(str(string))
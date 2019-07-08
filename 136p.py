e=input()
e=e.split()
q=int(e[0])
q1=int(e[1])
w=input()
w=list(map(int,w))
c=0
for i in w:
  if(q1==i):
    c=c+1
if(c>0):
  print("yes",c)

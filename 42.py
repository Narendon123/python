e=input()
e=e.split()
y=e[0]
t=e[1]
r=len(str(y))
l=len(str(t))
if(r<l):
    print(t)
elif(l<r):
    print(y)
else:
    print(y or t)

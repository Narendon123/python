d=input()
d=d.split()
z=input()
z=z.split()
z=list(map(int,z))
i=int(d[0])
f=int(d[1])

if(f in z):
    print("yes")
else:
    print("no")

e=input().split()
e1=int(e[0])
e2=int(e[1])
c=0
q=list(map(int,input().split()))
for i in q:
    if(e2==i):
        c=c+1
if(c>0):
    print("yes")
else:
    print("no")

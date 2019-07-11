r=input().split()
e1=int(r[0])
e2=int(r[1])
c=0
l=[]
l2=[]
q=list(map(int,input().split()))
for i in q:
    if(e2==i):
        l.append(i)
if(l!=[]): 
    print(*l)        
else:
    if(i<e2):
        l2.append(i)
        print(*l2)

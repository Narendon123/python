qt=input()
qt=qt.split()
q1a=str(qt[0])
q2a=int(qt[1])
l=[]
l2=[]
for i in q1a:
    l.append(i)
a=len(l)
if(q2a==1):
    print(*q1a,sep=" ".upper())
else:    
    for i in range(0,a,q2a):
        l2.append(l[i+1])
    print(*l2.upper())    

        

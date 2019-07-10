q=input()
q=q.split()
q1=str(q[0])
q2=int(q[1])
l=[]
l2=[]
for i in q1:
    l.append(i)
a=len(l)
if(q2==1):
    print(*q1,sep=" ")
else:    
    for i in range(0,a,q2):
        l2.append(l[i+1])
    print(*l2)    

        

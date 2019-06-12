q=input()
q=q.split()
w=list(q[0])
w2=list(q[1])
c=0
for i in range(0,len(w)):
    if(w[i]==w2[i]):
        c=c+1
if(c==len(w)-1):
    print("yes")
else:
    print("no")               

w=input().split()
w2=input().split()
l=[]
l2=[]
t=int(w[1])
t1=int(w[0])
l3=[]
for i in range(0,t1):
    if(int(w2[i])<t):
        l3.append(int(w2[i]))
        u=sorted(l3)
print(*u,sep=" ")
 

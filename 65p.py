w=int(input())
w2=input().split()
l2=[]
l2.append(w2)
l3=[]
for i in range(0,w):
    if(int(w2[i])<w):
        l3.append(int(w2[i]))
       
print(*l3,sep=" ")
 

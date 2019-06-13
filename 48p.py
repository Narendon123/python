w=int(input())
l=[]
for i in range(1,w+1):
    if(w%i==0):
        if(i%2!=0):
            l.append(i)
print(*l,sep=" ")
        

yy=int(input())
l=[]
for i in range(1,yy+1):
    if(yy%i==0):
        l.append(i)
print(*l,sep=" ")
        

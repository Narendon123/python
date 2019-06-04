p=input()
p=p.split()
p=list(p)
e=0
l3=[]
p1=int(p[0])
p2=int(p[1])
for i in range(p1+1,p2):
    if(i%2!=0):
        l3.append(i)
print(*l3,sep=" ")
  

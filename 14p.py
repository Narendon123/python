t=int(input())
r=input()
r=list(r)
l=[]
for i in r: 
    if(i!='a' and i!='e' and i!='i' and i!='o' and i!='u'):
        l.append(i)
    p=l[::-1]
print(*p,sep="")

s=input()
s=s.split()
s=list(map(int,s))
t=int(s[0])
f=int(s[1])
l=[]
for i in range(t,f+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
               break
        else:
           l.append(i)
print(*l,sep=" ")       

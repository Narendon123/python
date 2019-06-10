r=input()
r=r.split()
t=input()
t=t.split()
t=list(map(int,t))
k=int(r[0])       
f=int(r[1])
c=0
for i in t:
       if(f==i):
           c=c+1
print(c)       

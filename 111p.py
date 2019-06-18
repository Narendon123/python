w=input().split()
w2=input().split()
l,l3=[],[]
e,e2=int(w[0]),int(w[1])
for k in range(0,e):
    l.append(w2[k])
s=len(l)
v=w2[int(s)::]
for i in l:
    if i in v:
        l3.append(i)
        r=sorted(l3)
print(*r,sep=" ")

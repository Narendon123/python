q=int(input())
w=0
y=1
u=1
l5=[]
c=0
for i in range(0,q-1):
    p=w+y
    w=y
    y=p
    l5.append(str(p))
o=' '.join(l5)
print(u,o)

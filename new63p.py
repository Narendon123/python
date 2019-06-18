e=int(input())
w=input().split()
w2=input().split()
l=[]
l2=[]
l3=[]
for i in w:
    l.append(i)
for i in w2:
    l2.append(i)
for i in range(0,e):
    for j in range(0,e):
        if(l[i]==l2[j]):
            l3.append(l[i])
print(*l3,sep=" ")

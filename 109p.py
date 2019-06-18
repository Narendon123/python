w=int(input())
w2=list(map(int,input().split()))
l=[]
r=0
for i in range(0,w):
    r=r+w2[i]
    l.append(r)
print(*l[::-1]
 

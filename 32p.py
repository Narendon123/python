r=list(map(int,input().split()))
w=r[0]
w2=r[1]
c=0
e=list(map(int,input().split()))
for i in e:
    if(i==w2):
        c=c+1
if(c==1):
    print("Yes")
else:
    print("No")

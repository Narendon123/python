ix=int(input())
iy=list(map(int,input().split()))
temp=iy
a=sorted(iy)
if(temp==a):
    print("yes")
else:
    print("no")

b=int(input())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
if(c[::]==a[::-1]):
    print("yes")
else:
    print("no")


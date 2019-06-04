d=int(input())
s=0
for i in range(2,d//2):
    if(d%i)==0:
        s=s+1
if(s==0):
    print("yes")
else:
    print("no")

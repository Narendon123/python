g=int(input())
t=0
f=g
while(f>0):
    d=f%10
    t+=d**3
    f//=10
if g==t:
    print("yes")
else:
    print("no")


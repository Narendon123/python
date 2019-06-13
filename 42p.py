a=int(input())
w=input()
w=w.split()
e=sorted(w)
c=0
for i in w:
    if(i!=e):
        c=1
if(c==1):
    print("yes")
else:
    print("no")

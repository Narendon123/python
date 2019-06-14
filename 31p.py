r=input()
d=p=0
for i in r:
    if i=='(':
        d=d+1
    if i==')':
        p=p+1
if(p==d):
    print("yes")
else:
    print("no")

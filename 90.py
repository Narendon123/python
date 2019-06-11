r=input()
l=[]
for i in r:
    if(i.isdigit()==True):
        l.append(i)
print(*l,sep="")

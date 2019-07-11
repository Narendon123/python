b=input()
l=[]
l2=[]
b=b.split()
for i in b:
    l.append(int(i))
a=str(sum(l))
l2.append(a)
if(l2==l2[::-1]):
    print("YES")
else:
    print("NO")


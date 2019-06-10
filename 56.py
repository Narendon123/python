z=input()
c=0
g=0
for i in z:
    if(i.isalpha()==True):
        c=1
    elif(i.isdigit()==True):
        g=1
if(c==1 and g==1):
    print("Yes")
else:
    print("No")

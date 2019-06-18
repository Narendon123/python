w=input()
b=len(w)
c=0
for i in range(0,b):
    for j in range(i+1,b):
        if(w[i]==w[j]):
            c=c+1
            break
if(c>=1):
    print("yes")
else:
    print("no")


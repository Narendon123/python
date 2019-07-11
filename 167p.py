a=input()
a=a.replace(" ","")
e=len(a)
for i in range(2,e):
    if(e%i==0):
        print("no")
        break
else:
    print("yes")
        

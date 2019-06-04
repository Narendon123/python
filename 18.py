g=int(input())
fto=1
if(g<0):
    print("invalid")
elif(g<=1):
    print(1)
else:
    for i in range(1,g+1):
        fto=fto*i
    print(fto)

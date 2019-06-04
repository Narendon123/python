gm=int(input())
fto=1
if(gm<0):
    print("invalid")
elif(gm<=1):
    print(1)
else:
    for i in range(1,gm+1):
        fto=fto*i
    print(fto)

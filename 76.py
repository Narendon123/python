w=int(input())
r=0
if(w>1):
    for i in range(2,w//2):
        if(w%i==0):
            print("yes")
            break
else:
    print("no")

t=list(map(int,input().split()))
for i in range(1,(t[0]*t[1])+1):
    if(i%t[0]==0 and i%t[1]==0):
        print(i)
        break

a=int(input())
b=input()
b=b.split(' ')
b=list(map(int,b))
for i in range(0,len(b)):
    print(i,b[i])

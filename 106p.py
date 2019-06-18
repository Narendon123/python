w=int(input())
w2=list(map(int,input().split()))
values=dict.fromkeys(w2)
for i in values:
    print(i,end=" ")

g=int(input())
r=input()
r=r.split()
r=list(map(int,r))
a=sorted(r)
a=list(map(int,a))
avg=sum(a)//g
print(abs(avg))

q=input()
q=list(q)
q[::2],q[1::2]=q[1::2],q[::2]
print(*q,sep="")

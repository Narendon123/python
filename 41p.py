q=input()
q=q.split()
w=int(q[0])
e=int(q[1])
for i in range(0,w):
    if(e**i==w):
        print("yes")
        break
else:
    print("no")

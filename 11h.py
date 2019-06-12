w=input()
w=w.split(" ")
y=[]
for i in w:
    y.append(i[::-1])
print(*y,sep=" ")    

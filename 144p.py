s=int(input())
w=list(map(int,inpuit().split()))
g=[]
for i in range(0,s+1):
  if(w[i+1]%w[i]==0):
    g.append(w[i+1])
print(g)    

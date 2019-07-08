c=input()
c=list(map(int,c))
q=0
for i in c:
  if(i%2==0):
    q=q+1
if(q%2==0):
  print("E")
else:
  print("O")

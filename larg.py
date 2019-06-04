g=input()
g=g.split()
if(g[0]>g[1] and g[0]>g[2]):
    print(g[0])
elif(g[1]>g[0] and g[1]>g[2]):
    print(g[1])
else:
    print(g[2])      
          

d=input()
d=d.split()
l1=[]
for i in d:
    l1.append(i)
g=int(l1[0])
r=int(l1[1])
for num in range(g,r):
    ord=len(str(num))
    s= 0  
    te = num  
    while te > 0:  
        di = te% 10  
        s+= di**ord 
        te //= 10  
    if num == s:  
       print(num)  
 

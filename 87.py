w=input()
w=w.split()
a=int(w[0])
b=int(w[1])
i=1
while(i<=a and i<=b):
    if(a%i==0 and b%i==0):
        gcd=i
    i=i+1
print(gcd)    

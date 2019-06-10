p=input()
l=0
for i in range(len(p)):
    if(p[i].isalpha()!=True and p[i].isdigit()!=True):
        l=l+1
print(l)    

e=int(input())
if(e>-2**15+1 and e<2**15+1):
    print("INT")
elif(e>-2**31+1 and e<2**31+1):
    print("LONG")
else:
    print("INVALID")

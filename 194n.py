b=input()
b=b.split()
w=str(b[0])
w1=str(b[1])
if((w=='R' or w=='P') and (w1=='P' or w1=='R')):
    if(w==w1):
        print("D")
    else:
        print("P")
elif((w=='P' or w=='S') and (w1=='S' or w1=='P')):
    if(w==w1):
        print("D")
    else:
        print("S")
elif((w=='R' or w=='S') and (w1=='S' or w1=='R')):
    if(w==w1):
        print("D")
    else:
        print("R")

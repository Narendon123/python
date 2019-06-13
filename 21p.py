w=input().split()
w2=input().split()
w3=input().split()
if(w[0]==w2[0]==w3[0] or w[1]==w2[1]==w3[1] or (w[0]==w[1] and w2[0]==w2[1] and w3[0]==w3[1])):
    print("yes")
else:
    print("no")

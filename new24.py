def median(w):
    x=sorted(w)
    return x[(len(x)//2)]
d=int(input())
w=input()
w=w.split()
w=list(map(int,w))
print(median(w))

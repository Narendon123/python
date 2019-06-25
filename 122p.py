a=input()
a=a.split("-")
w=a[0]
w1=a[1]
w2=a[2]
aa=len(w)
bb=len(w1)
cc=len(w2)
d={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
if(aa==2 and bb==2 and cc==4 and int(a[0])>0 and int(a[0])<31 and int(a[1])>0 and int(a[1])<13):
    print(d[w1])   
   

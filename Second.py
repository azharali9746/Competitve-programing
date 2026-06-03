a=list(map(int,input().split()))
max1,max2=-1,-1

for i in a:
    
    if max1<i:
        max2=max1
        max1=i
    elif i!=max1 and i>max2:
        max2=i
print(max2)
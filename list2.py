l=list(map(str,input().split()))
l2=[]
for i in l:
    if l.count(i)%2!=0 and i  not in l2:
        l2.append(i)
print(l2)
#needed to print the list of elements that are present odd number of times in the list.
#the list is sorted in ascending order of odd numbers and then in descending order of even numbers

l=list(map(int,input().split()))
l.sort()
res=[]
for i in l:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
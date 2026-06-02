l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(i)    
for i in range(1,11):
    print(i)    

for i in l:
    l.remove(i)
print(l)

#op:[2, 4, 6, 8, 10
l2=l[2:6]
#op:[6, 8, 10]
l3=l[2:6:2]     
#op:[6, 10]
l4=l[::2]
#op:[2, 6, 10]  if we start from 0 then we get even index values
#if want to skip 2 values then we can use step as 3
l5=l[::3]
#op:[2, 8]  if we start from 0 then we get even index values

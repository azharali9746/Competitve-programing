n=int(input())
flag=0
if(n==0 or n==1):
    print("")
   
else:
    for i in range(2,int(n**0.5)+1): 
        if(n%i==0):
            flag=1
            break
if(flag==0):
    print("YES")
else:
    print("NO")
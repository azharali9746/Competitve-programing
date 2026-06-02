#1560A
t=int(input())
for i in range(t):
    n=int(input())
    i=0
    k=1
    while 1:
        if i%3!=0 and i%10!=3:
            if n==k:
                print(i)
                break
            k=k+1
        i=i+1
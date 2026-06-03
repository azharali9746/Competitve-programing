n=int(input())
l=list(map(int,input().split()))
police=0
unsolved=0
for i in l:
    if i==-1:
        if police>0:
            police=police-1
        else:
            unsolved=unsolved+1 
    else:
        police=police+i
print(unsolved)
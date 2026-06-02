a=int(input())
result=0;
while a>0 :
    rem=a%10
    result=result+rem*10
    a=a//10
print(result)
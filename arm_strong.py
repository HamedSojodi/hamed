def is_armstrong(n):
    sum =0
    temp=n
    while (temp > 0):
        rem = temp%10
        sum =sum +(rem *rem *rem)
        temp= temp //10

    if(n ==sum):
        yield "is armstrong"
    else:
        yield "NOT is armstrong"



m=list(is_armstrong(153))
for i in m:
    print(i, end='')

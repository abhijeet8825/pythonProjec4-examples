n=int(input('Enter length of the series\n'))
a,b=0,1
for i in range(1,n):
    c=a+b
    a=b
    b=c
    print(b)
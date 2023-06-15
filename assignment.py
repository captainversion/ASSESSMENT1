num = int(input("Enter the Range Number:"))
a= 0
b= 1
for n in range(1,num):
    if(n<=1):
        next = n
    else:
        next = a + b
        a=b
        b=next
    print(next)
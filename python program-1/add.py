num=int(input("Enter number:"))
sum=0
for i in range(1,num+1):
    if i<=num:
        sum=(sum+i)
        i=i+1
print("sum is:",sum)
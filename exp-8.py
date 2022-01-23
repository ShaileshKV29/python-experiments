num = int(input("Enter Number : "))
sum_n = 0
while num > 0:
    r = num%10
    sum_n += r
    num //= 10

print("Sum of Digits is : ", sum_n)
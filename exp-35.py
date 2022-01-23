nums = [213,23,4343,4343,54,544,65,65,7]
even_num = []
odd_num = []

for num in nums:
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)

print(nums)
print(even_num)
print(odd_num)
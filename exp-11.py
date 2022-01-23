num = list(set(input("Enter Num : ")))
for i in range(len(num)):
    num[i] = int(num[i])

max_item = max(num)
num.remove(max_item)
max2_item = max(num)

print("First Max : ", max_item)
print("Second Max : ", max2_item)
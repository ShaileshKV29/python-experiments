integers = input("Enter List of Integers(10) : ").split()
for i in range(len(integers)):
    integers[i] = int(integers[i])

int_sum = 0

for integer in integers:
    if integer % 2 != 0:
        int_sum += integer
    
print(f"Sum of Even Integers is {int_sum}")
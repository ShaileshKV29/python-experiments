dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

product = 1

for items in dict1.values():
    product *= items

print(f"Product is {product}")
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(dict1["a"])
dict1["b"] = "b"

print(f"Keys: {dict1.keys()}")
print(f"Values: {dict1.values()}")

print("\nKeys")
for items in dict1:
    print(items, end=" ")

print("\n\nValues")
for items in dict1:
    print(dict1[items], end=" ")

print()
print(dict1.items())

removed_value = dict1.pop("b", "Value not found")
print(dict1)
print(removed_value)

dict1["d"] = 40
print(dict1)
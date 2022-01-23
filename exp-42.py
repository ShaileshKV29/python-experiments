dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(f"Dictionary before removal {dict1}")
removed_value = dict1.pop("b", "No key Found")
print(f"Dictionary after removal {dict1}")
print(f"Element Removed : {removed_value}\n")

print(f"Dictionary before removal {dict1}")
removed_value = dict1.pop("d", "No key Found")
print(f"Dictionary after removal {dict1}")
print(f"Element Removed : {removed_value}")

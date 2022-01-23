from pprint import pprint


dict1 = {
    "name": "Shailesh",
    "age": 19,
    "phone": 9838410953
}

dict2 = {
    "address": "Prayagraj",
    "Sem": 4
}

dict3 = dict1 | dict2
dict4 = {**dict1, **dict2}
print(dict3)
print(dict4)
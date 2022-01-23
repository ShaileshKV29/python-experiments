f = open("./Exp-47/file.txt", "r")
text = list(f.read())
for item in text:
    print(item)
f.close()
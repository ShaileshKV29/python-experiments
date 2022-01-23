f = open("./Exp-49/file.txt", "r")
text = f.read()
print(text[::-1])
f.close()
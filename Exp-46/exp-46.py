f = open("./Exp-46/file.txt", "a")
f2 = open("./Exp-46/file.txt", "r")

for i in range(10):
    f.write(str(i))
f.close()
print(f2.read())
f2.close()


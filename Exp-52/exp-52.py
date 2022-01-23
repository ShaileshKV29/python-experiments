from itertools import count


f = open("./Exp-52/file.txt", "r")
text = list(f.read())
key = "s"
count_char = text.count(key)
print(text)
print(count_char)
f.close()
from cgi import test
from itertools import count


f = open("./Exp-51/file.txt", "r")
text = f.read().split()
print(text)
print(len(text))
f.close()
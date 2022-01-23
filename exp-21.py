string = list(input("Enter the String : ").lower())
vowels = ['a', 'e', 'i', 'o', 'u']
num_of_vowels = 0

for vowel in string:
    if vowel in vowels:
        num_of_vowels += 1

print(f"Number of Vowels is {num_of_vowels}")
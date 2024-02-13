# Example of 'for' using a str
parrot = "Norwegian Blue"

for character in parrot:
    print(character)

# Find the separators to print only digits from a string
number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))


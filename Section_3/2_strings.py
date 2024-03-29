# String can use single (' ') or double quotes (" ")
print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')

 # Concatenation of string
print("hello" + " world")

# Declaring variables to print a message
# Using 'input()' to get a name from the user
greeting = "Hello"
name = input("Please enter your name ")
print(greeting + " " + name)

age = 24
print(age)

# Using 'type()' to see the data type from a variable
print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
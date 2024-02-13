# Example of 'for' loop block of code
# for i in range(1, 3):
#     print("No.{0} squared is {1} and cubed is {2:4}"
#         .format(i, i ** 2, i ** 3))

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

# Example of 'if/else' block of code
if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))

# Example of 'elif' block of code
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")

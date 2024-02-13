#         012345678901234
parrot = "Norwegian Blue"

# Mini Challenge
# Add some code to the program, so that it prints out "we win"
# Each character should appear on a separete line.
# The program should get the charaters from the parrot string, using indexing.
# The 'w' is already printed out, you just need to print the remaing 5 characters.
# With the text that is already being printed, the final output from the program should be:
# Norwegian Blue
# w
# e
#
# w
# i
# n

# Using positive indexes
print(parrot)
print(parrot[3])    # w
print(parrot[4])    # e
print(parrot[9])    # 
print(parrot[3])    # w
print(parrot[6])    # i
print(parrot[8])    # n

# Using negative indexes, use the positive index - the string size
print()
print(parrot)
print(parrot[3 - 14])    # w
print(parrot[4 - 14])    # e
print(parrot[9 - 14])    # 
print(parrot[3 - 14])    # w
print(parrot[6 - 14])    # i
print(parrot[8 - 14])    # n

# Slicing the string from position [0] up to, but no includging position [6]
print()
print(parrot[0:6])      # Norweg
print(parrot[3:5])      # we
print(parrot[0:9])      # Norwegian
print(parrot[:9])       # Norwegian
print(parrot[10:14])    # Blue
print(parrot[10:])      # Blue
print(parrot[:])        # Norwegian Blue

# Slicing with negative indexes
print(parrot[-4:-2])
print(parrot[-4:12])

# Usin a Step in a Slice
print()
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223,372,036,854,775,807"
print(number[1::4])     # ,,,,,,
number = "9,223;372:036 854,775;807"
separators = number[1::4]     # ,;: ,;
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 Integer division, rounded down towards minus infinity
print(a % b)    # 0 module: the remainder after integer division

print()

# Using integer division to perform a for loop
for i in range(1, a // b):
    print(i)

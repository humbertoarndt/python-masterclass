empty_list = []
even = [ 2, 4, 6 ,8]
odd = [ 1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)

# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)

# digits = list("432985617")
# print(digits)

# more_numbers = list(numbers)      -> New list using list()
# more_numbers = numbers[:]         -> New list using slice
# more_numbers = numbers.copy()   #   -> New list using .copy()
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)


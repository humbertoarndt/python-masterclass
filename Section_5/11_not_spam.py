menu = [
    ["egg", "bacon"],
    ["egg","sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# Prints the original menu
print(">> OG MENU")
for meal in menu:
    print(meal)

# Prints the meal without removing "spam"
print("\n>> Menu without removing 'spam'")
for meal in menu:
    t_meal = []
    if "spam" not in meal:
        print(meal)
    else:
        for item in meal:
            if item != "spam":
                t_meal.append(item)
        print(t_meal)

# Prints the menu while removing "spam"
print("\n>> Menu removing 'spam'")
for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)
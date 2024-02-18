available = ["computer", "monitor", "keyborard", "mouse", "mouse mat", "hdmi cable", "dvd drive"]
current_choice = "-"
valid_choices = []

for i in range(1, len(available) + 1):
    valid_choices.append(str(i))
print(valid_choices)
computer_parts = [] # Create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now ontains: {}".format(computer_parts))
    else:
        print("Please add options from the list bellow")
        for number, part in enumerate(available):
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()
print(computer_parts)
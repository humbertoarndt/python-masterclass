menu = ["1. humberto", "2. doisberto", "3. tresberto"]

option = True

while option:
    print("Please, chose a partner:")
    for item in menu:
        print("\t{}".format(item))
    print("\t0. exit")
    answer = int(input())
    print(answer)
    if answer > len(menu):
        print("Error")
        break
    elif answer == 0:
        option = False
    else:
        print("Well done, now {} is your partner".format(menu[answer - 1]))
else:
    print("Bye bye")
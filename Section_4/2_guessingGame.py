answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # Guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("you got it first time")

# Challenge answer
if guess == answer:
    print("you got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:   # Guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guesses correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guesses correctly")
# else:
#     print("You got it first time")


# Challenge
# Write a small program to ask for a name and an age.
# When both values have been entered, check if the eprson is the right age to 
# go on an 18-30 holiday (They must be over 18 and under 31)
# If they are, welcome them to the holiday, otherwise print a (polite) 
# message refusing them entry
# Our program expect valid input. We'll see how to handle invlaid numbers, later
# in the course
# Remember that humans languages aren't always precise.
# Someone coutns as "Over 18" from 1 second after midnigth on their birtday
# Their actual age equal 18, but they're counted as being over 18 when 
# considering things like voting or getting a credit card

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Welcome {} into our holiday".format(name))
else:
    print("Sorry, by your age you are not allowed here")

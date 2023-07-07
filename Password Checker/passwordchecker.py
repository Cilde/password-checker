import string
from time import *

password = input("Please enter the password you desire to check:")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

with open('commonpasswords.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in a common list. Score reset to 0.")
    sleep(5)
    
    
if length > 8:
    score += 1
if length > 12:
    score +=1
if length > 16:
    score += 1
if length > 32:
    score +=1
print(f"Password length is {str(length)}, adding {str(score)} points!")

if sum(characters)> 1:
    score += 1
if sum(characters)> 2:
    score += 1
if sum(characters)> 3:
    score += 1

print(f"Password has {str(sum(characters))} different character types, your score is {str(score)} /7 ")

if score < 4:
    print(f"The password is weak! Please do not use it! Your score is {str(score)} / 7")
elif score == 4:
    print(f"The password is decent, but not great, your score is {str(score)} / 7")
elif score > 4 and score < 6:
    print(f"Your password is good, it would be classed as secure! Your score is {str(score)} / 7")
elif score > 6:
    print(f"Your password is great! It is likely to not be cracked. Your score is {str(score)} / 7")

sleep(5)
print("Closing...")

pass
pass
pass
pass
pass

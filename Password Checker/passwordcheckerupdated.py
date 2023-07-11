import string
from time import *


print(">>> ETHAN'S PASSWORD CHECKER! <<<")
print("")
password = input("Please enter the password you desire to check: ")
print("")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

length = len(password)

with open('passwords.txt', 'r') as f:
    common = f.read().splitlines()
if password in common:
    print("ALERT: PASSWORD FOUND IN COMMON LIST - DO NOT USE.")
    print("")
    print("---------------------")
    print("Press any key to exit")
    input("---------------------")
    exit()

score = 0
    
if length > 8:
    score += 1
if length > 12:
    score +=1
if length > 16:
    score += 1
if length > 32:
    score +=1
print(f"")

if sum(characters)> 1:
    score += 1
if sum(characters)> 2:
    score += 1
if sum(characters)> 3:
    score += 1

print(f">>> YOUR RATING <<<")
if score < 4:
    print(f"{str(score)} out of seven. This is a VERY BAD password.")
elif score == 4:
    print(f"{str(score)} out of seven. This is a BAD password.")
elif score > 4 and score < 6:
    print(f"{str(score)} out of seven. This is a DECENT password.")
elif score > 6:
    print(f"{str(score)} out of seven. This is a GOOD password.")

print('')
print('----------------------')
print('Press any key to exit.')
input('----------------------')
exit()

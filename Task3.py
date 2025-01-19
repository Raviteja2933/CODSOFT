#Password Generator
import random
import string
print("Welcome to random Password Generator!")
print("="*50)
length = int(input("Specify Length of Password: "))
print("="*50)
char = string.ascii_letters
char += string.digits
char += string.punctuation
password = ""
for i in range(length):
    next_character = random.choice(char)
    password += next_character
print("Your Random Password is: ",password)
print("="*50)
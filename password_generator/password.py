import random
import string

# Define parameter for the password to be generated
params =[]
random_letters = []
random_numbers = []
random_characters = []

letters = string.ascii_letters

# Getting input form user
params.append(int(input("How many letters do u want: ")))
params.append(int(input("How many numbers do u want: ")))
params.append(int(input("How many characters do u want: ")))


# Generating random letters, numbers and characters
for i in range(params[0]):
    random_letters.append(random.choice(letters))
for i in range(params[1]):
    random_numbers.append(random.randint(0,9))
for i in range(params[2]):
    random_characters.append(chr(random.randint(8208,15000)))


# Concatinating and shuffling all random letters, numbers, and characters
random_password = random_characters + random_letters + random_numbers
random.shuffle(random_password)

str_password = [str(x) for x in random_password]
password = ''.join(str_password)

print(password)
import random
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))


"""
# 1. Using "Random" lib module and built-in methods

password_list = []
for i in range(letters_count):
    password_list.append(random.choice(letters_list))

for i in range(symbols_count):
    password_list.append(random.choice(symbols_list))

for i in range(numbers_count):
    password_list.append(random.choice(numbers_list))

    
print(password_list)
random.shuffle(password_list)
print(password_list)

password2 = str()
for c in password_list:
    password2 += c

print(password2)
"""

# 2. More pythonistic solution
password_list = []
for i in range(letters_count):
    password_list.append(random.choice(letters_list))

for i in range(symbols_count):
    password_list.append(random.choice(symbols_list))

for i in range(numbers_count):
    password_list.append(random.choice(numbers_list))
print(password_list)

for i in range(len(password_list)):
    rand_index = random.randint(0, len(password_list)-1)
    rand_element = password_list.pop(rand_index)
    print(rand_element)
    password_list.append(rand_element)

print(password_list)

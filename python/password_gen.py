# Generates a secure password
# It includes at least 1 lower case letter, 
#       1 upper case letter and a number

import random

pw_size = 0

# Uncomment next line for quick tests without prompts
# pw_size = 8

while pw_size < 8 or pw_size > 30:
    print("Size of the password (between 8 and 30): ", end="")
    pw_size = int(input())

# ord("Z")
# 97 - 122
# 65 - 90
# chr(95)
pw_temp = []

# Lower case
for i in range(30):
    pw_temp.append(chr(random.randrange(97,123,1)))

# Upper case
for i in range(30):
    pw_temp.append(chr(random.randrange(65,91,1)))

# Numbers
for i in range(20):
    pw_temp.append(str(random.randrange(0,10,1)))

# Special chars
for i in range(10):
    pw_temp.append(chr(random.randrange(33,48,1)))

# Extract a lowercase letter, uppercase and a number
pw_temp2 = []
pw_temp2.insert(0, pw_temp[0])
pw_temp2.insert(1, pw_temp[30])
pw_temp2.insert(2, pw_temp[60])

random.shuffle(pw_temp)
pw_temp2 += pw_temp[:pw_size-3]
random.shuffle(pw_temp2)
pw_final = "".join(pw_temp2)

# print(pw_temp)
print(pw_final[:pw_size])
# random.randrange(1,3,1)

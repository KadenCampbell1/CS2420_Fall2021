import random

seed_value = 10
lyst = []

# # with open("rngNumbers.txt", 'w') as rngNumbers_txt:  # opens and adds random values to a text file
# #     i = 0
# #     while i < seed_value:
# #         rngNumbers_txt.write(str(random.randint(0, 5)) + "\n")
# #         i += 1
#
# with open("rngNumbers.txt", 'r') as rngNumbers_txt:  # opens and adds random values to a text file
#     lyst = [x.strip().split() for x in rngNumbers_txt.readlines()]

for i in range(seed_value):
    random_value = random.randint(0, 5)
    lyst.append(random_value)

print(lyst)

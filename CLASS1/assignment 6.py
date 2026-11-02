import random

code1 = random.randint(0,9), random.randint(0,9), random.randint(0,9)

code2 = random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)

print("3digit code: ", *code1)
print("4digit code: ", *code2)
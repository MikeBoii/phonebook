import random

x = random.randint(100000,1000000)

print(x)

sum = 0

while True:
    sum += x%10
    x = x//10
    if x == 0:
        break
    

print(sum)
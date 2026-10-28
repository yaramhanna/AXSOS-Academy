import random

def randInt(min=0, max=100):
    if min > max:
        min, max = max, min

    if max < 0:
        max = 0
    if min < 0:
        min = 0
        
    num = (random.random() * max - min) + min

    return round(num)


# 1. No arguments -> 0 to 100
print("Default (0 to 100):", randInt())

# 2. Only max provided -> 0 to 50
print("Max only (0 to 50):", randInt(max=50))

# 3. Only min provided -> 50 to 100
print("Min only (50 to 100):", randInt(min=50))

# 4. Both min and max provided -> 50 to 500
print("Both provided (50 to 500):", randInt(min=50, max=500))

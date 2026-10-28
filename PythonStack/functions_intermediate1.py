import random

def randInt(min=0, max=100):
    if min > max:
        temp = min
        min = max
        max = temp
        
    span = max - min
    
    num = (random.random() * span) + min
    
    integer_part = int(num) if num >= 0 else int(num) - 1
    decimal_part = num - integer_part
    
    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part


# 1. No arguments -> 0 to 100
print("Default (0 to 100):", randInt())

# 2. Only max provided -> 0 to 50
print("Max only (0 to 50):", randInt(max=50))

# 3. Only min provided -> 50 to 100
print("Min only (50 to 100):", randInt(min=50))

# 4. Both min and max provided -> 50 to 500
print("Both provided (50 to 500):", randInt(min=50, max=500))

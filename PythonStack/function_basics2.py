
# 1. Countdown
def countdown(num):
    result = []
    while num >= 0:
        result.append(num)
        num -= 1
    return result
print(countdown(5))


# 2. Print and Return
def print_return(my_list):
    print(my_list[0])
    return my_list[1]
print(print_return([1, 2]))


# 3. First Plus Length
def first_plus_length(my_list):
    count = 0
    for item in my_list:
        count += 1
    return my_list[0] + count
print(first_plus_length([1, 2, 3, 4, 5]))


# 4. Values Greater than Second
def values(my_list):
    if len(my_list) < 2:
        return False
        
    second_val = my_list[1]
    new_list = []
    for val in my_list:
        if val > second_val:
            new_list.append(val)
   
    print(len(new_list))
    return new_list
print(values([5, 2, 3, 2, 1, 4]))


# 5. This Length, That Value
def length_value(size, value):
    return [value] * size
print(length_value (4, 7))


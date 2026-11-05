
# 1. Countdown
def countdown(num):
    result = []
    while num >= 0:
        result.append(num)
        num -= 1
    return result
print(countdown(5))


# 2. Print and Return
def p_and_r(my_list):
    print(my_list[0])
    return my_list[1]
print(p_and_r([1, 2]))


# 3. First Plus Length
def fpl(my_list):
    count = 0
    for item in my_list:
        count += 1
    return my_list[0] + count
print(fpl([1, 2, 3, 4, 5]))


# 4. Values Greater than Second ()
def vgts(my_list):
    if len(my_list) < 2:
        return False
    
    second_val = my_list[1]
    new_list = []
    for val in my_list:
        if val > second_val:
            new_list.append(val)
    
    print(len(new_list))
    return new_list

print(vgts([5,2,3,2,1,4]))


# 5. This Length, That Value
def len_and_val(size, value):
    return [value] * size
print(len_and_val(4, 7))
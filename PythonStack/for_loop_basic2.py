
# 1. Biggie Size
def biggie_size(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x] = "big"
    return list
print(biggie_size([-1, 3, 5, -5]))

# 2. Count Positives
def count_positive(list):
    count = 0
    for x in list:
        if x > 0:
            count +=1
    list[len(list)-1] = count
    return list
print(count_positive([1, 6 ,-4, -2, -7, -2]))

# 3. Sum Total
def sum_total(list):
    total = 0
    for x in list:
        total += x
    return total
print(sum_total([1,2,3,4]))

# 4. Average
def average(list):
    if not list:
        return 0
    return sum(list)/len(list)
print(average([1,2,3,4]))

# 5. Length
def length(list):
    return len(list)
print(length([37,2,1,-9]))

# 6. Minimum 
def minimum(list):
    if not list:
        return False
    current_min = list[0]
    for number in list:
        if number < current_min:
            current_min = number
    return current_min
print(minimum([37,2,1,-9]) )

# 7. Maximum
def maximum(list):
    if len(list) == 0:
        return False
    max_val = list[0]
    for x in list:
        if x > max_val:
            max_val = x
    return max_val
print(maximum([37,2,1,-9]))


# 8. Ultimate Analysis
def ult(list):
    if not list:
        return {
            'length': 0,
            'sumtotal': 0,
            'average': 0,
            'minimum':False,
            'maximum':False,
        }
    total = sum(list)
    return{
        'sumTotal': total,
        'average': total/len(list),
        'minimum': min(list),
        'maximum': max(list),
        'length': len(list)
    }
print(ult([37,2,1,-9]) )

# 9. Reverse List
def rev(list):
    for x in range(len(list) // 2):
        list[x], list[len(list) - 1 - x] = list[len(list) - 1 - x], list[x]
        return list
print(rev([37,2,1,-9]))

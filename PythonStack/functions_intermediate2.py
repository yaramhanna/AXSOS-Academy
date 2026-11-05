
# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print('x =', x)

students[0]['last_name'] = 'Bryant'
print('students =', students)

sports_directory['soccer'][0] = 'Andres'
print("sports_directory =", sports_directory)

z[0]['y'] = 30
print("z =", z)


# 2. Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for item in some_list:
        output = ", ".join([f"{key} - {value}" for key, value in item.items()])
        print(output) 

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 


# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        # Check if the key exists in the current dictionary before printing
        if key_name in item:
            print(item[key_name])


# Example data from Part 2
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

print("First Names:")
iterateDictionary2("first_name", students)

print("Last Names:")
iterateDictionary2("last_name", students)


# 4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, val_list in some_dict.items():
        print(f"{len(val_list)} {key.upper()}")

        for value in val_list:
            print(value)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    }
printInfo(dojo)


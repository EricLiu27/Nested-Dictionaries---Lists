# 1. Update Values in Dictionaries and Lists

# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]


# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# sports_directory['basketball'][1] = "Bryant"
# print(sports_directory['basketball'])
# # In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][0] = "Andres"
# print(sports_directory['soccer'])
# # Change the value 20 in z to 30
# z[0]["y"] = 30
# print(z)

# 2. Iterate Through a List of Dictionaries

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# def iterateDictionary(some_list):
#     for i in range(0, len(some_list)):
#         print(
#             f"first_name - {students[i]['first_name']}, last name - {students[i]['last_name']}")


# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3. Get Values From a List of Dictionaries


# def iterateDictionary2(key_name, some_list):
#     for i in range(0, len(some_list)):
#         print(some_list[i][key_name])


# iterateDictionary2('last_name', students)


# 4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    
    for key in some_dict:
        print(len(some_dict[key]),key)
        for value in some_dict[key]:
            print(value)

printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

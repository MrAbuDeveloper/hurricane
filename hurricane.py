### 1 vazifa
# my_fav_dishes = ['osh', 'somsa', 'shashlik', 'norin']
#
# for item in my_fav_dishes:
#     print(f"My favorite dish is {item}")
#     # print("My favorite dish is " + item)

### 2 vazifa
# my_dishes = ['osh', 'somsa', 'shashlik', 'norin']
# friend_dishes = my_dishes.copy()
# friend_dishes_1 = my_dishes[:]
# friend_dishes_2 = [item for item in my_dishes]

# print(my_dishes)
# print(friend_dishes_2)
# my_dishes.append('steak')
# friend_dishes_2.append('olot somsa')
# print(my_dishes)
# print(friend_dishes_2)
### 3 vazifa
# user_num = input('Sonni kiriting: ')
# nums = [num for num in range(1, int(user_num)+ 1)]
# print(nums)
# result = 0
# for item in nums:
#     result += item
# print(result)
# print(sum(nums))

# num_odd = [item for item in range(1, 101) if item % 2 != 0]
# num_juft = [item for item in range(1, 101) if item % 2 == 0]
# print(num_odd)
# print(num_juft)

# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412,
#     566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
#     742, 717, 958, 743, 527
# ]
#
# result = []
# for num in numbers:
#     if num == 815:
#         break
#     else:
#         result.append(num)
#
# result.sort()
# print(result)

###set

# set_1 = set()
# set_1 = {1, 2, 3, 4, 5, 6, 1, 2, 4, 5, 6}
# set_2 = {}
# print(set_1)
# print(type(set_2))

### list.append()
### set.add()
### copy()
### clear()
# set_1 = {1, 2, 3}
# set_2 = {4, 2, 3, 5}
# print(set_1.difference(set_2))
###pop()

# set_1 = {1, 2, 3, 4, 5, 6, 7}
# list_1 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 1, 2, 1, 2, 3, 7]
# result = []
# for item in list_1:
#     if item not in result:
#         result.append(item)
# print(result)
# print(set_1.__sizeof__())
# print(list_1.__sizeof__() + result.__sizeof__())

###dict

# dict_1 = {}
# dict_2 = dict()
### dict = {"kalit": "qiymat"}
#
# komp_1 = 'Shoxruz'
# komp_3 = 'Ismoil'
# students = {"komp_1": "Shohruz", "komp_2": "Avazbek", "komp_3": "Ismoil", "komp_4": "Akmal"}
#
# print(students["komp_1"])
# print(students["komp_2"])
# print(students["komp_3"])

# managers = {
#     "0000888": "Ikrom",
#     "1234453": "Janna",
#     "7888213": "Malika"
# }

# print(managers["0000888"])
# managers["0000888"] = "Abdurayim"
# print(managers)

# managers["7777777"] = "Kolya"
# print(managers)

# users = {
#     1: {
#         "name": "Abdurahmon",
#         "lastname": "Qo'chqorov",
#         "age": 23
#     },
#     2: {
#         "name": "Ismoil",
#         "lastname": "Murodov",
#         "age": 18
#     }
# }
# print(users[2]['lastname'])

### dict method

# dct = {'key1': 'value1', 'key2': 'value2'}
# dct_2 = {'key3': 'value3', "key4": 'value4'}
# dct.clear()
# print(dct)
# copy = dct.copy()
# print(copy)
# print(dct.get('key1'))
# print(dct['key1'])

# dct.pop('key1')
# print(dct)
# dct.update(dct_2)
# print(dct)

# print(dct.values())

# for item in dct:
#     print(item)
# for key in dct.keys():
#     print(key)
# for value in dct.values():
#     print(value)

# for item in dct.items():
#     print(item)
# for key, value in dct.items():
#     print(key, value)

# items = ('key', 'value')
# keys, values = items
# print(keys, values)
# print(keys)

# a = 13
# b = 23
# a, b = 13, 23
# print(a)
# print(b)
# _, a = 13, 12
# print(a)
# print(_)

# user1 = {
#     'id': 1,
#     'name': "Vasya",
#     "lastname": 'Ivanov'
# }
#
# user2 = {
#     'id': 2,
#     'name': "Sasha",
#     "lastname": 'Kim'
# }
# user3 = {
#     'id': 3,
#     'name': "Jovlon",
#     "lastname": 'Raimov'
# }
# users = [user1, user2, user3]
#
# for user in users:
#     print(f"Userni id = {user['id']} ismi: {user['name']} familiyasi: {user['lastname']}")


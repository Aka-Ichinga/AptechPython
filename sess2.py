# import math
#
#
# x = 30
# print(math.cos(30))
#
#
# # Strings
# name = "John"
# m = r"""luke mom's "jfj. \nIs here"
# djdfdsfsdfhsdjfhsdjkf
# sdkdfksdfsdkfksdfk
# sdksdksdkksdksdkksd
# sdddkdkkdkdssdd
# """
#
# print("the sentence is" + m)
# f = m[:4]
# print(f)
#
# b = 'luke' not in m
# print(b)
#
# # print("The name is %s from Uyo. he is %s" %(name, name))
# print(f"My name is {name} i am {x} years old")

# c = m.count('luke')
# print(c)

m = [0, 2, 5, 7, 8]
a = [10, 11]
f = m[0:1]
d = m[1:3]
m.append(9)
m.insert(0, -1)
m.extend(a)
print(m)
# print(d, f, type(d), type(f))
# s = 'samuel'
# c = s[0]
# g = s[0:5]
# print(type(c), type(s), type(g))
user = {'name': "sam"}
print(user['name'])
user['age'] = 100
print(user)
print(user.get('gender', "Male"))

name = input('enter your name')
print(name)
amount = input('enter amount')
print(type(amount))
amount = float(amount)
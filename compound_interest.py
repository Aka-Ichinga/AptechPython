name = input('Enter Your Name?')
names = ['samuel', 'mark', 'luke']
surnames = ['Samuel', "David", "Moses"]

if name in names:
    print("Your first name is", name)
elif name in surnames:
    print('Your surname is', name)
else:
    print('Name not found')
# print(name)


def sum_to_n(number):
    """
    The sum of numbers from 1 to number
    :param number: Input parameter
    :return: sum of numbers
    """
    total = 0
    for i in range(1, number+1):
        print(i)
        total += i
    return total

# b = sum_to_n(10)
# print(b)

def greet(name, msg="Good Morning"):
    print(msg, name)


# greet('Sam', msg="welcome")
names = ['sam', 'david']
def greets(msg, *names):
    f = lambda n: print('hey', n)
    for name in names:
        f(name)
        print(msg, name)

# greets('Welcome', 'sam', 'mike')
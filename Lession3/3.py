from time import time

def prime(numbers):
    d = 2
    while d * d <= numbers and numbers % d != 0:
        d += 1
    return d * d > numbers


def time_decorators(func):
    def new_func(*args, **kwargs):
        start_time = time()
        print("Start: ", start_time)
        result = func(*args, **kwargs)
        stop_time = time()
        print("Stop: ", stop_time)
        print("Runtime: ", stop_time - start_time)
        return result
    return new_func


def expon(numbers, e):
    exp = [i ** e for i in numbers]
    return exp


def test_numbers(number_list, var):
    array2 = []
    if var == 1:
        [array2.append(x) for x in number_list if x % 2 != 0]
    elif var == 2:
        [array2.append(x) for x in number_list if x % 2 != 0]
    elif var == 3:
        [array2.append(x) for x in number_list if (prime(x) == True and x > 1)]
    return array2


print('Home work lession 3')
menu = int(input('Select optio1n: \n 1 - Exponentation numbers, 2 - Test numbers\n'))
if menu == 1:
    array = list(map(int, input('Input list: ').split()))
    e = int(input('Input exp: '))
    starttimer = int(input('Start timer? \n 1 - Yes, 2 - No\n'))
    print('Exponentiation list:\n')
    if starttimer == 1:
        timer = time_decorators(expon)
        print(timer(array, e))
    else:
        exp_list = [i ** e for i in array]
        print(exp_list)
elif menu == 2:
    array = list(map(int, input('Input list: ').split()))
    option = int(input('Select option: \n 1 - even, 2 - not even, 3 - prime\n'))
    starttimer = int(input('Start timer? \n 1 - Yes, 2 - No\n'))
    if starttimer == 1:
        timer = time_decorators(test_numbers)
        print(timer(array, option))
    else:
        print(test_numbers(array, option))
else    :
    print('Error')
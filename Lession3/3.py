from time import time

FILTER_EVEN = 'even'
FILTER_NOT_EVEN = 'odd'
FILTER_PRIME = 'prime'

def prime(numbers):
    d = 2
    while d * d <= numbers and numbers % d != 0:
        d += 1
    return d * d > numbers


def prime_check(func, numbers):
    return [x for x in array if (x > 1 and prime(x))]


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


def expon(*numbers, e):
    exp = [i ** e for i in numbers]
    return exp


def test_numbers(number_list, var):
    res = []
    if var == FILTER_EVEN:
        res = list(filter(lambda x: x % 2 == 0, number_list))
    elif var == FILTER_NOT_EVEN:
        res = list(filter(lambda x: x % 2 != 0, number_list))
    elif var == FILTER_PRIME:
        res = prime_check(prime, array)
    return res


print('Home work lession 3')
array = list(map(int, input('Input list: ').split()))
menu = int(input('Select optio1n: \n 1 - Exponentation numbers, 2 - Test numbers\n'))
if menu == 1:
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
    option = int(input('Select option: \n 1 - even, 2 - not even, 3 - prime\n'))
    if option == 1:
        starttimer = int(input('Start timer? \n 1 - Yes, 2 - No\n'))
        if starttimer == 1:
            timer = time_decorators(test_numbers)
            print(timer(array, FILTER_EVEN))
        else:
            print(test_numbers(array, FILTER_EVEN))
    if option == 2:
        starttimer = int(input('Start timer? \n 1 - Yes, 2 - No\n'))
        if starttimer == 1:
            timer = time_decorators(test_numbers)
            print(timer(array, FILTER_NOT_EVEN))
        else:
            print(test_numbers(array, FILTER_NOT_EVEN))
    if option == 3:
        starttimer = int(input('Start timer? \n 1 - Yes, 2 - No\n'))
        if starttimer == 1:
            timer = time_decorators(test_numbers)
            print(timer(array, FILTER_PRIME))
        else:
            print(test_numbers(array, FILTER_PRIME))
else:
    print('Menu item selection error!')

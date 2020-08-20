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
    exp = [i ** e for i in range(len(numbers) + 1)]
    exp = exp[1:]
    return exp


def test_numbers(number_list, var):
    array2 = []
    if var == 1:
        [array2.append(x) for x in range(len(number_list)) if x % 2 == 0]
        array2 = array2[1:]
    elif var == 2:
        [array2.append(x) for x in range(len(number_list)) if x % 2 != 0]
    elif var == 3:
        [array2.append(number_list[x]) for x in range(len(number_list)) if (prime(number_list[x]) == True and number_list[x] > 1)]
    return array2

def test_input(number):
    return number.isdigit()


print('Home work lession 3')
menu = str(input('Select option: \n 1 - Exponentation numbers, 2 - Test numbers\n'))
if test_input(menu) == True:
    if int(menu) == 1:
        array = list(map(int, input('Input list: ').split()))
        e = str(input('Input exp: '))
        if test_input(e) == True:
            e = int(e)
            starttimer = int(input('Start timer? \n 1 - Yes, 2 - No\n'))
            print('Exponentiation list:\n')
            if starttimer == 1:
                timer = time_decorators(expon)
                print(timer(array, e))
            else:
                print(expon(array, e))
        else:
            print('Error input expon')
    elif int(menu) == 2:
        array = list(map(int, input('Input list: ').split()))
        option = str(input('Select option: \n 1 - even, 2 - not even, 3 - prime\n'))
        if test_input(option) == True:
            starttimer = int(input('Start timer? \n 1 - Yes, 2 - No\n'))
            if starttimer == 1:
                timer = time_decorators(test_numbers)
                print(timer(array, option))
            else:
                print(test_numbers(array, option))
        else:
            print('Error input option')
    else:
        print('Error input menu')
else:
    print('Error input menu: only digit')
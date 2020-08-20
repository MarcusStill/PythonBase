from time import time

def expon(numbers, e):
    for i in range(len(numbers)):
        exp = int(numbers[i]) ** e
        print(exp, '\n')
    return exp

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

def test_numbers(number_list, var):
    array2 = []
    if var == 1:
        for i in range(len(number_list)):
            if int(number_list[i]) % 2 == 0:
                print(int(number_list[i]), end=' ')
    elif var == 2:
        for i in range(len(number_list)):
            if int(number_list[i]) % 2 != 0:
                print(number_list[i], end=' ')
    elif var == 3:
        for i in range(len(number_list)):
            if int(number_list[i]) != 1:
                if prime(int(number_list[i])) == True:
                    array2.append(int(array[i]))
        print(array2)

print('Home work lession 3')
print('Select optio1n: \n 1 - Exponentation numbers, 2 - Test numbers')
m = int(input())
if m == 1:
    print('Input list:')
    array = input().split()
    print('Input exp:')
    e = int(input())
    print('Start timer? \n 1 - Yes, 2 - No')
    t = int(input())
    print('Exponentiation list:\n')
    if t == 1:
        timer = time_decorators(expon)
        timer(array, e)
    else:
        expon(array, e)
if m == 2:
    print('Input list:')
    array = input().split()
    print('Select option: \n 1 - even, 2 - not even, 3 - prime')
    o = int(input())
    print('Start timer? \n 1 - Yes, 2 - No')
    t2 = int(input())
    if t2 == 1:
        timer = time_decorators(test_numbers)
        timer(array, o)
    else:
        test_numbers(array, o)
from time import time

# rewrote
def expon(numbers, e):
    exp = [i ** e for i in range(len(numbers) + 1)]
    exp = exp[1:]
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
                array2.append(int(array[i]))
        print(array2)
    elif var == 2:
        for i in range(len(number_list)):
            if int(number_list[i]) % 2 != 0:
                array2.append(int(array[i]))
        print(array2)
    elif var == 3:
        for i in range(len(number_list)):
            if int(number_list[i]) != 1:
                if prime(int(number_list[i])) == True:
                    array2.append(int(array[i]))
        print(array2)

print('Home work lession 3')
print('Select optio1n: \n 1 - Exponentation numbers, 2 - Test numbers')
menu = int(input())
if menu == 1:
    print('Input list:')
    array = input().split()
    print('Input exp:')
    e = int(input())
    print('Start timer? \n 1 - Yes, 2 - No')
    starttimer = int(input())
    print('Exponentiation list:\n')
    if starttimer == 1:
        timer = time_decorators(expon)
        print(timer(array, e))
    else:
        print(expon(array, e))
elif menu == 2:
    print('Input list:')
    array = input().split()
    print('Select option: \n 1 - even, 2 - not even, 3 - prime')
    o = int(input())
    print('Start timer? \n 1 - Yes, 2 - No')
    starttimer = int(input())
    if starttimer == 1:
        timer = time_decorators(test_numbers)
        timer(array, o)
    else:
        test_numbers(array, o)
else    :
    print('Error')
print('Home work lession 3')
print('Input list:')
array = input().split()
print('Input exp:')
e = int(input())
i = len(array)
print('Exponentiation list:')
for i in range(len(array)):
    exp = int(array[i]) ** e
    print(exp, end=' ')


def expon(numbers):
    for i in range(len(numbers)):
        exp = int(numbers[i]) ** e
        print(exp, end=' ')
    return exp

print('Home work lession 3')
print('Input list:')
array = input().split()
print('Input exp:')
e = int(input())
expon(array)


def prime(n):
    d = 2
    while d * d <= n and n % d != 0:
            d += 1
    return d * d > n

array3=[]
print('Input list:')
array2 = input().split()
print('Select option: \n 1 - even, 2 - not even, 3 - prime')
o = int(input())
if o == 1:
    for i in range(len(array2)):
        if int(array2[i]) % 2 == 0:
            print(int(array2[i]), end=' ')
elif o == 2:
        for i in range(len(array2)):
            if int(array2[i]) % 2 != 0:
                print(array2[i], end=' ')
elif o == 3:
        for i in range(len(array2)):
            if int(array2[i]) != 1:
                if prime(int(array2[i])) == True:
                    array3.append(int(array2[i]))
        print(array3)
import itertools
from time import time


# version with map
def degree(a, b=2):
    power = list(map(pow, range(a), itertools.repeat(b)))
    print(power)


# version without map
def rate():
    a = int(input('Enter the number of digits: '))
    b = int(input('Enter degree: '))
    result = []
    for i in range(a):
        result.append(i ** b)
    return result


print(rate())


# even, uneven, prime func
def stopwatch(func):
    def wrapper():
        start = time()
        func()
        end = time()
        time_taken = end - start
        print(f"time taken: {time_taken:.1f}")

    return wrapper()


@stopwatch
def different_number():
    CHOICE = int(input('choose operation:\n' '1: even\n' '2: uneven\n' 'Enter number: '))

    if CHOICE == 1:
        even = int(input('Enter the number of digits: '))
        result = []
        for i in range(even):
            if i % 2 == 0:
                result.append(i)
        print(f"even numbers: {result}")
        return result
    elif CHOICE == 2:
        uneven = int(input('Enter the number of digits: '))
        result = []
        for i in range(uneven):
            if i % 2 != 0:
                result.append(i)
        print(f"uneven numbers: {result}")
        return result


@stopwatch
def prime_num():
    prime = int(input('Enter the number of digits: '))
    result = []
    for num in range(prime):
        simple = True
        for i in range(2, num):
            if num % i == 0:
                simple = False
        if simple:
            result.append(num)
    print(f"prime numbers: {result}")
    return result


if __name__ == '__main__':
    degree(10)

import math
import time

start_time = time.time()


def gcd_subtract(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a + b


def gcd_modulo(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def gcd_recursive(a, b):
    if a == 0 or b == 0:
        return a + b
    else:
        if a > b:
            return gcd_recursive(a % b, b)
        else:
            return gcd_recursive(a, b % a)


print(gcd_recursive(219387123, 123123123928103822))

print("--- %s seconds ---" % (time.time() - start_time))

"""
89 is the first number with more than one digit, that when it digits are raised
 to the power of their index, they return the same number.
89 = 8^1 + 9^2
The next number with this property is 135
135 = 1^1 + 3^2 + 5^3
Write a function to collect these numbers,
that takes two integers a, b that defines the range [a, b] (inclusive)
and outputs a list of the sorted numbers in the range that fulfills the property described above.
Eg: sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""


def eureka(n):
    result = 0
    b = str(n)
    for x in range(len(b)):
        result += ((int(b[x])) ** (x + 1))
        print result
    if result == n:
        return True
    else:
        return False


print eureka(2427)


def sum_dig_pow(a, b):
    lists = [i for i in range(a, b + 1) if eureka(i)]
    return lists

# print sum_dig_pow(359, 2917)

def sum_dig_pow(a, b):
    results = []
    for num in range(a, b+1):
        for digit in str(num):
            t = 0
            n = int(digit) ** (str(num).index(digit)+1)
            t += n
            if n == num:
                results.append(num)
    return results

def factors(n, result=[]):
    for i in range(1, n):
        if n % i == 0:
            result.append(i)

    return result

factors(15)
print(factors(16))
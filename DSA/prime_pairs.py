def prime_pairs(n):
    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    result = []

    for a in range(2, n // 2 + 1):
        b = n - a

        if is_prime(a) and is_prime(b):
            result.append([a, b])

    return result


# CALL FUNCTION
print(prime_pairs(18))
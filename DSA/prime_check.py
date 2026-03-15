from DSA.fact_count import find_factors_count


def prime_check(N):
    factors = find_factors_count(N)
    if factors == 2:
        return True

    return False


print(prime_check(13))
print(prime_check(21))
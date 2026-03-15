
def find_factors_count(num):
    factor_count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            if i != num / i:
                factor_count += 2
            else:
                factor_count += 1

    return factor_count



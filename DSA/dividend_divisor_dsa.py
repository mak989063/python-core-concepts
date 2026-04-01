def divide(dividend: int, divisor: int) -> int:
    res_ls = []
    divid = abs(dividend)
    divis = abs(divisor)
    while divid > divis:
        if dividend < 0 or divisor < 0:
            res_ls.append(-1)
        else:
            res_ls.append(1)

        divid -= divis

    return (sum(res_ls))

print(divide(70000000, -3))
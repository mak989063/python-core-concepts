t = 7
def calc_simple_interest(p, n):
    global t
    simple_interest = p * n * t / 100
    return simple_interest

print(calc_simple_interest(1000, 2))

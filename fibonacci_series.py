def fib(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0,1]
    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    print(f"fibonacci series for first {n} numbers is as follows:")
    return fib_list

print(fib(10))
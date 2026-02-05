def road_tax(price):
    tax = None
    # YOUR CODE GOES HERE
    if price > 100000:
        tax = 0.20
    elif price > 75000:
        tax = 0.15
    elif price > 50000:
        tax = 0.10
    else:
        tax = 0.05

    return round(price * tax, 1)

print(road_tax(75000))
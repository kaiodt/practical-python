# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as f:
    # Skip headers
    next(f)

    # Calculate total cost
    total = 0.0

    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total += nshares * price

    print(f'Total cost: $ {total:.2f}')

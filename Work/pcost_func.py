# pcost_func.py
#
# Exercise 1.30-1.31


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        # Skip headers
        next(f)

        # Calculate total cost
        total = 0.0

        for line in f:
            row = line.split(',')

            try:
                nshares = int(row[1])
                price = float(row[2])
                total += nshares * price
            except ValueError:
                print("Couldn't parse", line)

    return total

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: $ {cost:.2f}')

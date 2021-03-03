# pcost_func_csv.py
#
# Exercise 1.32-1.33

import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        
        # Skip headers
        next(rows)

        # Calculate total cost
        total = 0.0

        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total += nshares * price
            except ValueError:
                print("Couldn't parse", row)

    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: $ {cost:.2f}')

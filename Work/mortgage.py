# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0

while principal > 0:
    month += 1
    principal = principal * (1 + rate/12) - payment
    total_paid += payment

    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    if principal < 0:
        total_paid += principal
        principal = 0.0

    # print(month, round(total_paid, 2), round(principal, 2))
    print(f'{month} {total_paid:.2f} {principal:.2f}')

# print('Total paid', round(total_paid, 2))
# print('Months', month)
print(f'Total paid: {total_paid:.2f}')
print(f'Months: {month}')

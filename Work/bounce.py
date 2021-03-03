# bounce.py
#
# Exercise 1.5

height = 100
height_variation = 3/5

for bounce in range(1, 11):
    height *= height_variation
    print(bounce, round(height, 4))

# 1) purpose statement: This function takes two numbers and returns the smaller of the two.
# signature: float float-> float
def min_of_2(x, y):
    if x < y:
        return x
    else:
        return y


# 2) purpose statement: This function takes three numbers and returns the smaller of the three.
# signature: float float float -> float
def min_of_3(x, y, z):
    if min_of_2(x, y) < z:
        return min_of_2(x, y)
    else:
        return z


# 3) purpose statement: This function takes a number representing days late a rental item and return the number of dollars for the assessed late fee by the given table.
# signature: int -> int
def rental_late_fee(x):
    if 0 <= x <= 2:
        return 0
    elif 2 < x <= 5:
        return 10
    elif 5 < x <= 12:
        return 15
    elif 12 < x <= 22:
        return 30
    elif x > 22:
        return 100
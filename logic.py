# 1) purpose statement:This function takes an integer and returns True when the integer is odd.
# signature: int -> bool
def is_odd(x: int):
    odds = ((x % 2) == 1)
    return odds


# 2) purpose statement:This function takes an integer and returns True when the integer falls in the given intervals.
# signature: int -> bool
def in_an_interval(x: int):
    intervals = (-10 <= x < -4) or (-2 <= x <= 8) or (27 < x < 52) or (10 < x <= 22) or (110 <= x <= 237)
    return intervals


# 3) purpose statement:This function takes two integers and returns True when the first integer is in the [75,140] interval and is divisible to the second integer which is in the interval (30,200]
# signature: int int-> bool
def is_divisible_in_interval(x, y):
    divisibles = (-75 <= x <= 140) and (30 < y <= 200) and (x % y == 0)
    return divisibles

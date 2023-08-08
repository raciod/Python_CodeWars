
import math

def find_next_square(sq):
    sqrt_n = math.sqrt(sq)
    if sqrt_n.is_integer():
        next_sqrt = int(sqrt_n) + 1
        next_square = next_sqrt ** 2
        return next_square
    else:
        return -1


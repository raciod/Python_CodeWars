import math

def is_square(n): 
    if n >= 0: 
        x = math.sqrt(n)
        return int(x) == x
    else:
        return False


    

n_1 = 5
print(is_square(n_1))

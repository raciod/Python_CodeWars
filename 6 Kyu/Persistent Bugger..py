def persistence(n):  
    count = 0
    n = str(n)
    print(type(n))
    while len(n) > 1:
        if len(n) == 2:
            p_1 = int(n[0])
            p_2 = int(n[1])
            n = str(p_1 * p_2)
        else:
            product = 1
            for digit in n:
                product *= int(digit)
            n = str(product)
        count += 1
    return count

# Test case
print(persistence(999))
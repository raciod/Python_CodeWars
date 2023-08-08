def series_sum(n):
    n = int(n)
    p = 1
    s = 0
    while n > 0 :
        x  = 1/ p 
        p += 3
        n -= 1
        s += x
    return f"{s:.2f}"
print(series_sum(1))


def digitize(n):
    result = []
    for l in reversed(str(n)) :
        result.append(int(l))
    return result
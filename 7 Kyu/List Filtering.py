def filter_list(l):
    result = []
    for i in l :
        if not (type(i) == str or i < 0 ) :
            result.append(i)
    return result



l = [1,2,'a','b']

print(filter_list(l))
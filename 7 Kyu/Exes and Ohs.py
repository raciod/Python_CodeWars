def xo(s):
    s = s.lower()
    count_x = 0
    count_o = 0
    if ("x" and "o") not in s  :
        return True
    else:
        for l in s:
            if l == "x":
                count_x += 1
            elif l == "o" :
                count_o += 1
        if count_x == count_o :
            return True
        else:
            return False

# Or 

def xo(s):
    s = s.lower()
    count_x = s.count('x')
    count_o = s.count('o')
    return count_x == count_o
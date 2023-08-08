def abbrev_name(name):
    words = name.split(' ')
    l_1 = words[0][0]
    l_2 = words[1][0]
    return f"{l_1.capitalize()}.{l_2.capitalize()}"


name = "patrick feeney"
print(abbrev_name(name))
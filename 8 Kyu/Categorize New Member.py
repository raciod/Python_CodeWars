def open_or_senior(data):
    output = []
    for mumb in data:
        if mumb[0] >= 55 and mumb[1] > 7:
            x = "Senior"
        else:
            x = "Open"
        output.append(f"[{x}]") # add 
    return output

data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(data))


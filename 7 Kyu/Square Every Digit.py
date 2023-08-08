def square_digits(num):
    num = int(num)
    result = ""
    for l in str(num):
        result += f"{str(int(l)**2)}"
    return int(result)

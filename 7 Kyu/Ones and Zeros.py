def binary_array_to_number(arr):
    n = 0
    sum = 0
    for bin in reversed(arr) :
        sum+= bin * (2 ** n)
        n+=1
    return sum

arr = [0, 0, 0, 1]
print(binary_array_to_number(arr))

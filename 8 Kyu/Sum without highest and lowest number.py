def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    else:
        return sum(arr) - max(arr) - min(arr)




arr = { 6, 2, 1, 8, 10 }
arr_2 = { 1, 1, 11, 2, 3 }


print(sum_array(arr))
print(sum_array(arr_2))
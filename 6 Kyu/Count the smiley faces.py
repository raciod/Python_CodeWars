def count_smileys(arr):
    v_s = [":-)", ":-D" , ":~)", ":~D",";-)", ";-D" , ";~)", ";~D",":)", ":D" , ";)", ";D"]
    count = 0
    for i in arr:
        if i in v_s :
            count+=1
    return count
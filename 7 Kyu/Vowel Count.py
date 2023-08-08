def get_count(sentence):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O',  'U']
    count = 0
    for l in sentence:
        if l in vowel :
            count +=1
    return count


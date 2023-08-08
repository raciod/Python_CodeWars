def high(x):
    max_score = 0
    highest_word = ""
    alphabet_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    words = x.split(" ")
    for word in words :
        score = 0
        for letter in word:
            if letter in alphabet_dict:
                score += alphabet_dict[letter]
        if score > max_score :
            max_score = score
            highest_word = word
        elif score == max_score:
            if x.index(word) < x.index(highest_word):
                highest_word = word

    return highest_word



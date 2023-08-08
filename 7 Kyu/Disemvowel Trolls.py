def disemvowel(string_):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O',  'U']
    for l in string_:
        if l in vowel :
            string_ = string_.replace(l, "")
    return string_
    
string_ = "This website is for losers LOL!"
print(disemvowel(string_))

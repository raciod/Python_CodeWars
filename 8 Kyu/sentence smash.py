###########################

# #_Problem_:

"""
Sentence Smash

Write a function that takes an array of words 
and smashes them together into a sentence and 
returns the sentence. You can ignore any need 
to sanitize words or add punctuation, but you 
should add spaces between each word. 
Be careful, there shouldn't be a space at 
the beginning or the end of the sentence!
"""

# #_solution :
def smash(words):
    sentence = ""
    for item in words:
        sentence += item + " "
    return sentence.strip()

# Example usage:
my_array = ['hello', 'world', 'this', 'is', 'great']
print(smash(my_array))

#######################################################
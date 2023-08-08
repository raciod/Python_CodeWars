def reverse_words(string):
    words = string.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Test cases
print(reverse_words("This is an example!"))  # Output: "sihT si na !elpmaxe"
print(reverse_words("double  spaces"))       # Output: "elbuod  secaps"
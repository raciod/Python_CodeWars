def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False
    
print(solution('abc', 'bc')) # returns true
print(solution('abc', 'd' )) # returns false
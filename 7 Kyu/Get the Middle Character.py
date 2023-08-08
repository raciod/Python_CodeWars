def get_middle(s):
    if len(s) % 2 == 1 :
        return s[int((len(s)-1)/2):int((len(s)-1)/2)+1]
    else:
        return s[int((len(s)-2)/2):int((len(s)-1)/2)+2]
    
s = "rachid"
print(get_middle(s))
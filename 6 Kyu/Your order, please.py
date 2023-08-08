def order(sentence):
    num = ( "1" , "2" ,"3", "3", "4", "5", "6", "7", "8", "9")
    result = []
    
    words = sentence.split(' ')
    for word in words:
        for l in word :
            if l in num :
                index = int(l)-1
                while index >= len(result):
                    result.append('')
                result[index] = word

    result_sentence = ' '.join(result)
    return result_sentence



sentence = "4of Fo1r pe6ople g3ood th5e the2"
print(order(sentence))
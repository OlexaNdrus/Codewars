def duplicate_encode(word):
    decoded_str=[]
    word=word.lower()
    for i in word:
        if word.count(i)>1:
            decoded_str.append(')')
        else:
            decoded_str.append('(')
    return ''.join(decoded_str)


print(duplicate_encode(input()))
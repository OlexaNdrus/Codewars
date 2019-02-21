def first_non_repeating_letter(string):
    # for i,j in enumerate(string):
    #     if j.lower() not in string[i+1:].lower() and j.lower() not in string[:i].lower():
    #         return j

    for i in string:
        if string.lower().count(i.lower())==1:
            return i
    return ''


print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))
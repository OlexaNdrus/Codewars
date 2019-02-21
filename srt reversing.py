import string

def reverse_letter(stringer):
    new_str=[]
    for i in stringer:
        if i in string.ascii_letters:
            new_str.append(i)
    return ''.join(reversed(new_str))

print(reverse_letter(input()))
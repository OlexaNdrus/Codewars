import string

def is_pangram(s):
    for let in string.ascii_lowercase:
        if not let in s.lower():
            return False
    return True

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
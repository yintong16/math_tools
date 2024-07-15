import timeit
import _string


def only_letters(X, case=None):
    X = ''.join(c for c in X if c in string.ascii_letters)

    if len(X) == 0:
        return None
    
    if case is None:
        return X
    elif case == "lower":
        return X.lower()
    elif case == "upper":
        return X.upper()

def shift_char(char, shift):
    if char in string.ascii_lowercase:
        base = 'a'
    elif char in string.ascii_uppercase:
        base = 'A'
    # It's not clear what shifting should mean in other cases
    # so if the character is not upper or lower-case, we leave it unchanged
    else:
        return char
    return chr((ord(char)-ord(base)+shift)%26+ord(base))


def shift_string(X, shift):
    return ''.join(shift_char(char, shift) for char in X)


def vigenere(X, key, case='upper'):
    X = only_letters(X, case = case)
    cipher = ''
    key_len = len(key)
    for i in range(len(X)):
        cipher = cipher + chr((ord(X[i]) - 65 + key[i%key_len])%26+65)
    return cipher
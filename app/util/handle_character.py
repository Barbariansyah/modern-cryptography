''' Handling capital letter '''


def letter_base_number(letter):
    return 65 if letter.isupper() else 97


def standardize_key(text_letter, key_letter):
    if text_letter.isupper() and key_letter.islower():
        key_letter = key_letter.upper()
    elif text_letter.islower() and key_letter.isupper():
        key_letter = key_letter.lower()

    return key_letter


def get_order(c, base_number=97):
    return (ord(c)-base_number)


def get_char(i, base_number=97):
    return (chr(i+base_number))

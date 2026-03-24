def simple_string_hash(text):
    total = 0
    for char in text:
        total += ord(char)
    return total

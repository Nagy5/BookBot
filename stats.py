import string

def get_text(text):
    words = text.split()
    return len(words)

def char_count(text):
    sol = {}
    for letter in text:
        l = letter.lower()
        if l.isalpha():
            if l not in sol:
                sol[l] = 0
            sol[l] += 1
    return sol
     

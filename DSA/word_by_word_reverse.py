
def reverse_words(s):
    s= s.strip()
    i = len(s) - 1
    word = ""
    words = []

    while i >= 0:
        if s[i] == " ":
            words.append(word)
            word = ""
        else:
            word = s[i] + word
        i -= 1

    words.append(word)

    return " ".join(words)

s = "xdq hv"
print(reverse_words(s))


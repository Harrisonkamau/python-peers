def abbreviate(phrase):
    out = ""

    for i in phrase.upper().split():
        out += i[0]

    return out

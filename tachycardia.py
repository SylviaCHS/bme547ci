def is_tachycardic(word):

    word_lc = word.lower()
    result = word_lc.find('tachycardic')

    if result == -1:
        output = bool(0)
    else:
        output = bool(1)
    return output

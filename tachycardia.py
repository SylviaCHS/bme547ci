def is_tachycardic(word):

    word_lc = word.lower()
    result = word_lc.find('tachycardic')

    if result == -1:
        output = "False"
    else:
        output = "True"
    return output


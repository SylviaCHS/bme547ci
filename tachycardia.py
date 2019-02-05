def is_tachycardic(word):
    result = word.find('tachycardic')

    if result == -1:
        output = "False"
    else:
        output = "True"
    return output


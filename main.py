import re


def camel_case(name):
    operation, method, word = name.split(';')
    if operation == 'S':
        list_of_words = re.sub(r"([A-Z])", r" \1", word).lower()
        if method == "M":
            return list_of_words.replace('()', '')
        else:
            return list_of_words
    elif operation == 'C':
        word_list = word.split()
        camel_case_word = ''.join([word_list[0]] + [w.capitalize() for w in word_list[1:]])
        if method == "M":
            return camel_case_word.replace(' ', '') + "()"
        else:
            return camel_case_word.replace(' ', '')


w = "S;C;OrangeHighlighter"
print(camel_case(w))

bad_words = ['badword1', 'badword2', 'badword3']
personal_info = ['phone', 'email', 'address', 'name']


def dict_filter(text):
    words = text.split()
    filtered_words = []
    for word in words:
        if word.lower() in bad_words:
            filtered_words.append('[BLEEP]')
        elif word.lower() in personal_info:
            filtered_words.append('[PERSONAL INFO]')
        else:
            filtered_words.append(word)
    return ' '.join(filtered_words)
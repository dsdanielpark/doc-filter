import re

phone_number_pattern = r'\d{2,3}-\d{3,4}-\d{4}'
email_pattern = r'[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|org)'
swear_words_pattern = r'(badword1|badword2|badword3)'

def re_filter(text):
    text = re.sub(phone_number_pattern, '[PHONE NUMBER]', text)
    text = re.sub(email_pattern, '[EMAIL]', text)
    text = re.sub(swear_words_pattern, '[BLEEP]', text)
    return text
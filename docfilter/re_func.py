# 정규함수 관련 전처리 모음

import re

def delete_parenthesis(x):
    text = re.sub(pattern= '\([^)]*\)', repl='', string= x)
    return ' '.join(text.split())  

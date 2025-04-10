'''
Kata URL: https://www.codewars.com/kata/56833b76371e86f8b6000015/
'''
import re
def to_cents(amount):
    price_pattern = r'\$\s*[\d]+(\.\d{2})'
    valid = re.compile(r'\$?\s*[\d]+(\.\d{2})?')
    if re.fullmatch(price_pattern, amount):
        return int(amount[1:].replace('.',''))
    else:
        return None
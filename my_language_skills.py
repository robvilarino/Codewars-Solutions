'''
Kata URL: https://www.codewars.com/kata/5b16490986b6d336c900007d
'''
def my_languages(results):
    ofthejedi = []
    r_list = sorted(results.items(), key=lambda x: x[1], reverse=True)
    for langScore in r_list:
        if langScore[1] >= 60: ofthejedi.append(langScore[0])
    return ofthejedi
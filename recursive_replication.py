'''
Kata URL: https://www.codewars.com/kata/57547f9182655569ab0008c4
'''
#@countcalls #uncomment, needed for testing kata on site
def replicate(times, number) -> list:
    if times <= 0:
        return []
    else:
        return [number] + replicate(times-1, number)
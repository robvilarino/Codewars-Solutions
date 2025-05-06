'''
Kata URL: https://www.codewars.com/kata/5274e122fc75c0943d000148
'''
def group_by_commas(n):
    
    x = 0
    rs = ""
    
    for num in str(n)[::-1]:
        if x % 3 == 0 and x != 0:
            rs += "," + num
        else:
            rs += num
        x += 1
    
    return rs[::-1]
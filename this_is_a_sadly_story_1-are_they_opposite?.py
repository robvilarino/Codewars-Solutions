'''
Kata URL: https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7
'''
def is_opposite(s1,s2): 
    if s1 == "" or s2 == "" or len(s1) != len(s2):
        return False
    
    for c in range(len(s1)):
        if s1[c].isupper():
            if s2[c].isupper(): return False
        else:
            if s2[c].islower(): return False
    
    return True
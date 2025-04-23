'''
Kata URL: https://www.codewars.com/kata/5667525f0f157f7a0a000004
'''
def bucket_of(said):
    
    d = {0:"air", 1:"water", 2:"slime", 3:"sludge"}
    w = ["water", "wet", "wash"]
    s = ["i don't know", "slime"]
    r = 0
    
    if any(w_w in said.lower() for w_w in w):
        r+=1
    if any(s_w in said.lower() for s_w in s):
        r+=2

    return d[r]
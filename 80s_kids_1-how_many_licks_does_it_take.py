'''
Kata URL: https://www.codewars.com/kata/566091b73e119a073100003a
'''
def total_licks(env):
    l = 252
    tcv = 0
    cm = ""

    if env:
        for k in env.keys():
            l += env[k]
            if env[k] > tcv:
                tcv = env[k]
                cm = f" The toughest challenge was {k}."
    
    m = f"It took {l} licks to get to the tootsie roll center of a tootsie pop."
    if tcv: m += cm
    
    return m
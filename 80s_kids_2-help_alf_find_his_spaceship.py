'''
Kata URL: https://www.codewars.com/kata/5660aa3d5e011dfd6e000063
'''
def find_spaceship(astromap):
    if "\n" in astromap:
        am = astromap[::-1].split("\n")
        for i in range(len(am)):
            if "X" in am[i]: 
                z= am[i][::-1].index("X")
                return [z, i]
        return "Spaceship lost forever."
    else:
        if "X" in astromap: 
            return [astromap.index("X"),0]
        else:
            return "Spaceship lost forever."
'''
Kata URL: https://www.codewars.com/kata/5fde1ea66ba4060008ea5bd9
'''
def burner(c,h,o):
    hrem = h%2
    hpairs = int((h/2) if h%2 == 0 else (h-1)/2)
        
    if hpairs >= o:
        water = o
        h = ((hpairs-o)*2) + hrem
        o = 0
    else:
        water = hpairs
        o = o-hpairs
        h = hrem

    orem = o%2
    opairs = int((o/2) if o%2 == 0 else (o-1)/2)
    
    if opairs >= c:
        CO2 = c
        o = ((opairs-c)*2) + orem
        c = 0
    else:
        CO2 = opairs
        c = c-opairs
        o = orem
    
    hrem = h%4
    hquads = int(h/4 if h%4 == 0 else ((h-hrem)/4))
    
    if hquads >= c:
        methane = c
        h = ((hpairs-c)*2) + hrem
        c = 0
    else:
        methane = hquads
        c = c-hquads
        h = hrem

    return water,CO2,methane
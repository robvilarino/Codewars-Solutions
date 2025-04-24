'''
Kata URL: https://www.codewars.com/kata/5662292ee7e2da24e900012f
'''
def get_socks(name, socks):
    
    if not socks: return []
    
    sock_inv={}
    
    for color in set(socks):
        sock_inv[color] = socks.count(color)
    
    if name == "Punky":
        first_sock_color = "" 
        for color in sock_inv.keys():
            if sock_inv[color] > 0:
                if first_sock_color: return [first_sock_color, color]
                first_sock_color = color
    
    elif name == "Henry":
        for color in sock_inv.keys():
            if sock_inv[color] > 1:
                return [color, color]
    
    return []
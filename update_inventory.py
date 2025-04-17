'''
Kata URL: https://www.codewars.com/kata/57a31ce7cf1fa5a1e1000227
'''
def update_inventory(cur_stock, new_stock):
    rdict = {}
    ret_list = []
    
    for ep in cur_stock:
        rdict[ep[1]] = ep[0]
        
    for np in new_stock:
        if np[1] not in rdict.keys():
            rdict[np[1]] = np[0]
        else:
            rdict[np[1]] += np[0]
            
    for tp in sorted(rdict.keys()):
        ret_list.append((rdict[tp],tp))
        
    return ret_list
'''
Kata URL: https://www.codewars.com/kata/55b95c76e08bd5eef100001e/python
'''
def count_arara(n):
    ans = []
    
    num_adaks = int(n/2)
    bool_anane = n%2
    
    if num_adaks > 0: 
        ans.append("adak "*num_adaks)
        if bool_anane: ans.append("anane")
        else: ans[-1] = ans[-1][:-1]
    else: ans.append("anane")
    
    print(ans)
    
    return "".join(ans)

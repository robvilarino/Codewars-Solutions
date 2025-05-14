'''
Kata URL: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
'''
def wave(people):
    r = []
    if not people: return r
    
    for i in range(len(people)):
        
        if people[i] == " ":
            continue
        
        if i == 0:
            r.append(people.capitalize())
        elif i != len(people)-1:
            r.append(people[0:i] + people[i].upper() + people[i+1:])
        else:
            r.append(people[:-1]+people[i].upper())
    
    return r
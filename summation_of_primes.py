'''
Kata URL: https://www.codewars.com/kata/59ab0ca4243eae9fec000088
'''
def summation_of_primes(primes):
    if primes <= 1: return 0
    
    pl =[]
    
    for i in range(2,primes+1):
        isPrime = True
        if i == 2:
            pl.append(i)
            continue
        for p in pl:
            if i % p == 0:
                isPrime=False
                break
        if isPrime: pl.append(i)
        
    return sum(pl)
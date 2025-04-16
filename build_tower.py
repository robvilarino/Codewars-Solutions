'''
Kata URL: https://www.codewars.com/kata/576757b1df89ecf5bd00073b
'''
def tower_builder(n_floors):
    tower = []
    width = (2*n_floors)-1
    
    for floor in range(0,n_floors):
        stars = 1 + (2*floor)
        padding_length = (width - stars)//2
        tower.append(" "*padding_length + "*"*stars + " "*padding_length)
    return tower
'''
Kata URL: https://www.codewars.com/kata/57675f3dedc6f728ee000256
'''
def tower_builder(n_floors, block_size):
    
    tower = []
    bl = block_size[0]
    bh = block_size[1]
    width = bl+((2*bl)*(n_floors-1))
    
    for floor in range(0,n_floors):
        line = ("*"*(bl + (2*(bl*floor)))).center(width)
        for i in range(0,bh):
            tower.append(line)
    
    return tower
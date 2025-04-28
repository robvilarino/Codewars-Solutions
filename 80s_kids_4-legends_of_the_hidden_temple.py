'''
Kata URL: https://www.codewars.com/kata/56648a2e2c464b8c030000bf
'''
def mark_spot(n):
    
    if not isinstance(n, int) or n%2==0 or n<1: return "?"
    if n == 1: return "X\n"
    
    r = [] # Will return a joined list of strings
    center_width = 3+((n-3)*2) # Spaces between X for each line
    start_width = 0 # Spaces preceeding the first X on any given line, 0 at first
    
    # Will make the first half of the X and the middle sing X
    for x in range(n, ((n+1)//2)-1, -1):
        
        # This is the middle of the big X
        if x == ((n+1)//2): 
            r.append(" "*start_width+"X\n") # Will always be a single X with set number of spaces before
        else: 
            r.append(" "*start_width +"X" + " "*center_width +"X\n")
            center_width -=4
            start_width +=2

    # Go backward from the middle of the array to complete the symmetrical X
    for y in range(((n+1)//2)-2, -1, -1):
        r.append(r[y])

    # Return list as one string joined
    return "".join(r)
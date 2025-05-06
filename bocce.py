'''
Kata URL: https://www.codewars.com/kata/55332880e679dd9cb3000081
'''
from math import sqrt

def bocce_score(balls):
    
    # Distances from jack for each teams balls will be stored here
    g = {"black": [], "red": []}
    
    # Initiate variables for ball coords
    b_y = b_x = 0
    
    # Grab the coords for the jack
    j_y = balls[-1]["distance"][0]
    j_x = balls[-1]["distance"][1]
    
    # "Distance Finder" - 
    # lambda function for pythagorean calc from coords
    df = lambda x, y: sqrt((x**2) + (y**2))
    
    # Iter to each ball in the balls list
    for ball in balls:
        
        # Dont include the jack
        if ball["type"] != "jack":
            
            # Grab each coord for the ball
            b_y = ball["distance"][0]
            b_x = ball["distance"][1]
            
            # Do pythagorean calc to get distance
            # Distance is a float
            g[ball["type"]].append(df((j_y-b_y), (j_x-b_x))) 
    
    # Sort the distances
    g["black"].sort()
    g["red"].sort()
    
    # Determine winning team if there is one
    # If there isn't return the no points texts
    if g["black"][0] < g["red"][0]:
        wnr = "black"
        lsr = "red"
    elif g["red"][0] < g["black"][0]:
        wnr = "red"
        lsr = "black"
    else:
        return "No points scored"
    
    # Initiate score int var
    s = 0
    
    # Check how many winning team balls 
    # were closer than losing teams closest ball
    for dis in g[wnr]:
        if dis < g[lsr][0]: s += 1
    
    # Return winning team and how much they scored
    return f"{wnr} scores {s}"
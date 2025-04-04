'''
kata url: https://www.codewars.com/kata/59eb28fb0a2bffafbb0000d6/
'''

def sort_by_binary_ones (numList): 
    # Sort with the three conditions as tuple in lambda
    numList.sort(key=lambda numStr: ((str(bin(int(numStr)))[2:].count("1")*-1), len(str(bin(int(numStr)))[2:]), int(numStr)))     
    return numList
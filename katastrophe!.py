'''
Kata URL: https://www.codewars.com/kata/55a3cb91d1c9ecaa2900001b
'''
import numpy as np
def strong_enough(e, age): return "Needs Reinforcement!" if float(sum(e[0])*sum(e[1])*sum(e[2])) > (1000 * np.exp(-0.01 * age)) else "Safe!"
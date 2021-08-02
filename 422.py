from sympy import *

x, y = symbols("x y", real=True)
hyperbola = 12*x**2 + 7*x*y - 12*y**2 - 625 # Sympy assumes this is equal to 0
hyp1, hyp2 = solve(12*x**2 + 7*x*y - 12*y**2 - 625, y) # Two halves of the hyperbolic relation

def find_intersection(expr): # expr represents the function of the line to intersect with the hyperbola
    return solve(hyp1 - expr, x) + solve(hyp2 - expr, x)

# Unsolved. It is clear that this "brute-force" method will not work on account of time
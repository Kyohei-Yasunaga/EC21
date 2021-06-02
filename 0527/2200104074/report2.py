import numpy as np
import sympy

theta=sympy.var('theta',real=True)

x1 = 2
y1 = 0

x2 = 5 * np.sin(2 * theta)
y2 = 5 * np.cos(2 * theta)

x3 = 10 * np.sin(theta)
y3 = 10 * np.cos(theta)
S=(x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

print(S)

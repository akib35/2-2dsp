from numpy import *
from sympy import *
a = numpy.arange(10)
x = sympy.symbols('x')
expr = sin(x)
f = lambdify(x, expr, "numpy")
print(f(a))

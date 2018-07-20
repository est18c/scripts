from sympy import *

x = Symbol('x')
y = Symbol('y')
limit(sin(x)/x, x, 0)

expand(cos(x+y), trig=True)

simplify((x+x*y)/x)

diff(sin(x), x)

series(cos(x), x)

integrate(exp(-x**2)*erf(x), x)

integrate(exp(-x**2), (x, -oo, oo))

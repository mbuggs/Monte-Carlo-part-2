Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... 
... def MonteCarlo_double(f, g, x0, x1, y0, y1, n):
...     """
...     Monte Carlo integration of f over a domain g>=0, embedded
...     in a rectangle [x0,x1] -by- [y0,y1]. n^2 is the number of
...     random points.
...     """
...     
...     x = np.random.uniform(x0, x1, n)
...     y = np.random.uniform(y0, y1, n)
...     
...     f_mean = 0
...     num_inside = 0  
...     for i in range(len(x)):
...         for j in range(len(y)):
...             if g(x[i], y[j]) >= 0:
...                 num_inside = num_inside + 1
...                 f_mean = f_mean + f(x[i], y[j])
...     f_mean = f_mean/num_inside
...     area = num_inside/(n**2)*(x1 - x0)*(y1 - y0)
...     return area*f_mean

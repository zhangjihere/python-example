# -*- coding: utf-8 -*-
# python

from pprint import pprint

# a complex number
cc=complex(3, 4)
cc2=3+4j
pprint(cc)
pprint(cc2)

pprint(cc==cc2)
pprint(cc+cc2)
pprint(cc+2j)

pprint(cc.real)
pprint(cc.imag)

# length of a complex number. That is, Sqrt[ i**2 + j**2 ] 
pprint(abs(complex(3,4)))

import cmath
z1=complex(0, 1)
# get polar coordinary. Return this form (length, angle)
pprint(cmath.polar(z1))
# polar to rectangular. Input is (length, <angle in radius>). Returns a complex number
z2=cmath.rect(1, cmath.pi)
pprint(z2)


pprint(cmath.pi) # 3.14159265359
pprint(cmath.e)  # 2.71828182846

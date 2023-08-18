correct = 0

## 1.
# se billede

## 2.
# Oxygen -2     : 
# Ruthenium +3  : Husk 4d5
correct += 1

## 3.  
# se billede

## 4.
# se billede
correct += 1

## 5.
correct += 1

## 6.
# se billede

## 7.
from sympy import *
x = symbols("x")
molalitet = (5 / x) / 0.205
konstant = 20 # C / m
frysepunktsforøgelse = 4
lign1 = Eq(frysepunktsforøgelse, konstant * molalitet)
# print(solve(lign1))

correct += 1

## 8.

## 9.
masse = (16 / 21) / 2 # mol/L
# print(masse)
lign1 = Eq(0.92 * ((masse - 2*x)**2), (x * (3*x**3)))
# print(lign1)
# print(solve(lign1))
x_solved = solve(lign1)[1]
# print(masse - 2 * x_solved, x_solved, 3 * x_solved)

# 10
NaOH = 100000 / (22.99 + 15.999 + 1.008)
HF = 100000 / (18.99 + 1.008)
AlOH = 100000 / (25.981 + 3 * 15.999 + 3 * 1.008)
# print(2 * NaOH, HF, 6 * AlOH)
produceret = NaOH / 3
produceret_g = produceret * (3 * 22.989 + 26.98 + 6 * 18.99)
# print(produceret_g)
correct += 1

# 11.
stofmængde = 1.5 * 2.5 # mol
masse = stofmængde * (14.007 + 4 * 1.008 + 14.007 + 3 * 15.999)
nitrogen_masseprocent = (2 * 14.007) / (14.007 + 4 * 1.008 + 14.007 + 3 * 15.999)
nitrogen_masse = masse * nitrogen_masseprocent
masseprocent = nitrogen_masse / 2500
# print(masseprocent * 100, "%")

# 12.
correct += 1

# 13
molarmasse = 12.011 + 2 * 39.09 + 3 * 15.999
mol_kaliumcarbonat = 25 / molarmasse
# print(mol_kaliumcarbonat)
T = 200 * 273.15
p = 1
R = 0.0821
V = (mol_kaliumcarbonat * R * T)/p
# print(V)

# 14.
correct += 1

# 15. 
konc_so3 = 4.79 * 0.1 * 0.1**(1/2)
# print(konc_so3)
correct += 1

# 16.
# Eddikesyre: CH3COOH
import math
vægt = 320
molarmasse = 2 * 12.011 + 2 * 15.999 + 4 * 1.008
stofmængde = vægt / molarmasse
pka = 4.76
ka = 10**(-pka)
lign1 = Eq(ka, (x**2)/(stofmængde-x))
pH = -math.log10(solve(lign1)[1])
print(pH)
correct += 1

# 17.

# 18.
correct += 1

# 19.

# 20.
correct += 1


## ## ## 
print("-------------------")
print(f"{correct}/{20} correct = {round(correct*100/20, 2)}%")
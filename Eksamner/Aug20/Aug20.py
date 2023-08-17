
total = 20
correct = 0

## 1.
# 6, 10, 10

## 2.
lys_hastighed = 3 * 10**8 # m / s
planks_konstant = 6.63 * 10**(-34) # J*s
energi = 1521 * 10**3 # J/mol
avogradros_tal = 6.022 * 10**23 # mol-1
bølgelængde = planks_konstant * lys_hastighed / (energi / avogradros_tal)
# print(bølgelængde, "m")

# 3. 
# Jo højere bindingsorden, jo korterer bindingslængde
correct += 1

# 4. 
# Se billede

# 5.
# Marker alle funktionelle grupper, og løs opgaven
# Keton og Amid findes ikke i de to stoffer
correct += 1

# 6.
# Se billede

# 7.
# NaCl
molar = 0.2
konstant = 1.86 # C / m for vand se table 13.2
frysepunktsforøgelse = konstant * molar
frysepunktsforøgelse *= 2
frysepunkt = 0 - frysepunktsforøgelse
# print("NaCl", frysepunkt, "C")

# molar * frysepunktsforøgelse skal være så højt som muligt:
# print("NaCl", 0.2 * 2)
# print("CaCl2", 0.15*3)
# print("CH2OH CH2OH", 0.25)
# print("FeCl3", 0.12 * 4)
# print("CH4N2O", 0.3)
correct += 1

import math
from sympy import *
import numpy as np
x = symbols("x")
# 8.
# k = A * exp(-E_a / (R*T))
# Ea = aktiveringsenergien (J/mol)
# R = gaskonstant (8.314 J/K*mol)
# T = Absolut temperatur (K)
# A = frekvensfaktoren (s-1)
T1 = 30 + 273.15
T2 = 50 + 273.15
R = 8.314
Ea = 85 * 1000 # J/mol
k1 = 8 * 10**(-4)
k2 = k1 / np.exp(Ea / R * ((T1-T2) / (T1*T2)))

halveringstid = np.log(2)/k2
# print("Halveringstid: ", halveringstid)
correct += 1

# 9.
# K = (C^c*D^d) / (A^a*B^b)
# Omregning til gas (idealgasligningen):
T = 300 + 273.15
R = 0.0821 # L * atom / (mol * K)
V = 1 # L
pA = 0.11 * R * T / V
pB = 1.91 * R * T / V
pAB = 0.25 * R * T / V

k = (pA * pB ** 3) / (pAB ** 2)
# print("k: ", k)

# 10.
# Afstem reaktionsligning: 2NaCl + 2H2O -> 2NaOH + Cl2 + H2
T = 25 + 273.15
R = 0.0821 # L * atom / (mol * K)
p = 1
NaCl_molarmasse = 22.99 + 35.45
NaCl_molar = 1000 / NaCl_molarmasse
n = NaCl_molar / 2
V = n * R * T / p
# print("V:", V, "L")
correct += 1

# 11.
# Husk H2O samt H+
# 6 + 6 + 6 + 3 = 19
correct += 1

# 12:
grader_celcius = 25
p = 2 # atm
R = 0.081
V = 2 # L
T = (grader_celcius + 273.15) # K
n = p * V / (R * T)
# print(f"{n = } mol")
n2_molarmasse = 14.007 * 2
n2_gram = n2_molarmasse * n
# print(f"{n2_gram = } g")
correct += 1

# 13:
# gibbs = produkter - reaktanter # aflæs fra appendix 2
gibbs = (4 * -394.4 + 6 * -237.2) - (2 * -32.89)
# print(gibbs, "kJ/mol")

# 14: 
# q = m * s * deltaT = C * deltaT
# ved konstant tryk: delta H = q
# dermed Delta H = m * s * deltaT
vands_specifikke_varmekapacitet = 4.184 # J/(g*C) # tabel 6.2
m_vand = 1000 # g
antal_mol = 1
deltaH = -132.5 * 1000 # kJ/mol
temp_ændring = (deltaH * antal_mol) / (vands_specifikke_varmekapacitet * m_vand)
# print(f"{temp_ændring = } C")

# 15:
konc_h = 10**(-1.5)
konc_oh = 10**-14 / konc_h 
# print(f"{konc_oh = }")
correct += 1

# 16:
pKa = 9.3
Ka = 10**(-pKa)
stofmængde = 0.5
lign1 = Eq(Ka, (x * x) / (stofmængde - x))
pH = -math.log10(solve(lign1)[1])
# print(f"{pH = }")
correct += 1

# 17:
# Hg se spændingsrækken
correct += 1

# 18:
# Br2 + Pb <-> 2Br- + Pb2+
katode = 0.77
anode = -0.14
total = katode - anode
F = 96500 # C/mol
n = 2
gibbs = -n*F*total # J / mol
R = 8.314 # J / (K * mol)
T = 25 + 273 # K # 273.15 giver åbenbart ikke rigtigt??
# DeltaG = -R*T*ln(K)
K = math.exp(-gibbs/(R*T))
print(K)

# metode 2 til 18
K = math.exp(2*total/0.0257)
print(K)
correct += 1

# 19:
# se billede


# 20: 
# se billede
correct += 1




## ## ## 
print("-------------------")
print(f"{correct}/{20} correct = {round(correct*100/20, 2)}%")
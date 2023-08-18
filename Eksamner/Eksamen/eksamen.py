# 08077

# 1.
# 2 + 2 + 6 + 2 + 3 = 15
# nr. 15 er P

# 2. 
h = 6.626 * 10**(-34) # J*s
c = 3.00 * 10**8 #m/s
E = 4.2 * 10**(-19) # J
lamb = h * c / E
# print(lamb * 10**9, "nm")
# 473: synligt lys

# Testproblem fra bogen:
h = 6.626 * 10**(-34) # J*s
c = 3.00 * 10**8 #m/s
E = 3.98*10**(-21) # J
lamb = h * c / E
# print(lamb * 10**9, "nm")
# print(5 * 10**4)
# da disse er lig med hinanden, må det være korrekt (s. 212 i bogen)

# 3.
# se papir

# 4.
# finder elektronnegativitetsforskellen
# se papir

# 5. 
# se papir

# 6.
vands_vægt = 0.99 # decimaltal af totalt vægt
molarmasse = 22.99 + 35.45 # g/mol
molar = 10 / molarmasse
molalitet = molar / vands_vægt
konstant = 1.86 # C / m
frysepunktsforøgelse = konstant * molalitet
# Husk Van't Hoff faktor: 
frysepunktsforøgelse *= 1.9
frysepunkt = 0 - frysepunktsforøgelse
# print(frysepunkt, "C")
# -0.61 C

# 7.
na = 6.0221415 * 10**23
mol_lit = 1 / 6.94
unit_cells = (mol_lit / 2) * na
# print(unit_cells)
# 4.33 * 10**22

import math
# 8.
k = 3.18 * 10 **(-4) # s-1
T = 298 # K
A = 5.11 * 10**13
R = 8.314 #J/K*mol
Ea = -math.log(k/A) * (R * T) # J/mol
# print(Ea / 1000, "kJ/mol")
# 98

# 9.
N2 = 8.5 * 10**(-1)
H2 = 3.1 * 10**(-3)
NH3 = 3.1 * 10**(-2)
k = (NH3**2) / (N2 * H2**3)
# print(k)
# 37950.66 = 3.8 * 10**4

# 10.
vægt_NH3 = 18.1
vægt_CuO = 90.4
NH3_molarmasse = 14.007 + 3 * 1.008
CuO_molarmasse = 15.999 + 63.546
NH3_stofmængde = vægt_NH3 / NH3_molarmasse
CuO_stofmængde = vægt_CuO / CuO_molarmasse
N2_molarmasse = 2 * 14.007
# print(NH3_stofmængde / 2)
# print(CuO_stofmængde / 3)
# CuO stofmængde er lavest
N2_stofmængde = CuO_stofmængde / 3
vægt_N2 = N2_stofmængde * N2_molarmasse
# print(vægt_N2)
# 10.6 g

# 11.
mol_AgNO3 = 0.100 * 1.5
mol_NaCl = mol_AgNO3
molarmasse_NaCl = 22.99 + 35.45
vægt_NaCl = mol_NaCl * molarmasse_NaCl
# print(vægt_NaCl)
# umiddelbart er forholdet 1:1
# 8.76 g

# 12.
nitromethan_vægt = 5.0
nitromethan_molarmasse = 12.011 + 3 * 1.008 + 14.007 + 2 * 15.999
nitromethan_stofmængde = nitromethan_vægt / nitromethan_molarmasse
forhold = 5/4
o2_stofmængde = nitromethan_stofmængde * forhold

R = 0.0821 # 8.314
p = 0.2
T = 25 + 273.15 # K
n = o2_stofmængde
V = n * R * T / p
# print(V)
# 12.5 L / min

# 13.
vol_methan = 2.8
T_methan = 25 + 273.15
p_methan = 1.65
R = 0.0821
n_methan = (vol_methan * p_methan) / (R * T_methan)

vol_o2 = 35
T_o2 = 31 + 273.15
p_o2 = 1.25
R = 0.0821
n_o2 = (vol_o2 * p_o2) / (R * T_o2)

# print(n_methan, n_o2 / 2)
R = 0.0821 # 8.314
p = 2.5
T = 125 + 273.15 # K
n = n_methan
V = n * R * T / p
# print(V)
# 2.47 = 2.5

# 15
# E0_cell = (0.0257 V)/n * ln(K)
from sympy import *
x = symbols("x")
R = 8.314 # J / (K * mol)
T = 25 + 273 # K # 273.15 giver åbenbart ikke rigtigt??
F = 96500 # C/mol
e = 0.17 - (-0.5)
n = 2
k = math.exp((e * n * F) / (R * T))
# print(k)
k = math.exp((e * n)/0.0257)
# print(k)

# 16.
# pka = 3.5 * 10**(-8)
# k = 10**(-pka)
k = 3.5 * 10**(-8)
lign1 = Eq(k, (x * x * x ** 2) / (0.5 - x))
# print(solve(lign1))
h_konc = solve(lign1)[1]
pH = -math.log10(h_konc)
# print(pH)

# 17.
# print(10**(-4.76))
ka = 6.2 * 10**(-10)
hcn_volume = 100 / 1000 # L 
hcn_molær = 50 / 1000 # M
naoh_volumen = 500
# print(naoh_volumen)
hcn_stofmængde = hcn_molær / hcn_volume # mol
molar_cn_minus = hcn_stofmængde / (100 + naoh_volumen) * 1000
lign1 = Eq(ka, x**2 / (molar_cn_minus - x))
# print(solve(lign1))
h_konc = solve(lign1)[1]
ph = -math.log(h_konc)
# print(ph)

# Testproblem
ka = 1.8 * 10 **(-5)
acid = 0.100 * 25 / 1000
naoh_volume = acid * 1000 / 0.1
mol = acid / (25 + naoh_volume) * 1000
print(mol)
lign1 = Eq(ka, x**2 / (mol - x))
h_konc = solve(lign1)[1]
ph = -math.log(h_konc)
# print(ph)



# 19
# se papir

# 20
# se papir
import math
from sympy import *
x = symbols("x")
## ## ## 
# Beregn koncentrationen af [H3O+] i en opløsning hvor [OH-] = 3,4 · 10-4 M.
konc_OH = 10**-14 / (3.4 * 10**-4)
# print(konc_OH)

## ## ## 
# Hvad er pH i en 0,1 M HCl opløsning?
# pH = -log [H3O+] = -log 0,1 M = 1
pH = -math.log10(0.1)
# print(pH)

## ## ## 
# Hvad er pOH i en 0,01 M NaOH opløsning?
pOH = -math.log10(0.01)
# print(pOH)

## ## ##
# Hvad er pH i en 2 M KOH opløsning?
pOH = -math.log10(2)
pH = 14 - pOH
# print(pH)

## ## ##
# Beregn pH i en opløsning af 0.036 M salpeter-syrling, Ka = 4.5 * 10-4

#            HA     H+  A-
# Start:    0.036   0   0
# Ændring:  0.036-x x   x
# Dermed bliver formlen: 
Ka = 4.5 * 10**-4
lign1 = Eq(Ka, (x * x) / (0.036 - x))
# print(solve(lign1))
# Dermed er konc af H+ = 0.0038
pH = -math.log10(0.0038)
# print(pH)

## ## ##
# En syre, HA, opløses i vand med koncentrationen 0,3 M. Ka for syren er 1,6 · 10-4 M. 
# Hvad er koncentrationen af H+ ved ligevægt?
Ka = 1.6 * 10**-4
lign1 = Eq(Ka, (x * x) / (0.3 - x))
# print(solve(lign1))

## ## ##
# Hvad er pH i en 1 M opløsning af eddikesyre? pKa for eddikesyre er 4,8.
pKa = 4.8
Ka = 10**(-pKa)
lign1 = Eq(Ka, (x * x) / (1 - x))
# print(solve(lign1))
pH = -math.log10(solve(lign1)[1])
# print(pH)

## ## ##
# 50 ml 2 M ammoniakvand (NH3, pKb = 4,74) blandes med 50 ml vand. Hvad bliver pH?
konc = 2 / 2 # Da ammoniakvand fylder halvdelen af volumen
pKb = 4.74
Kb = 10**(-pKb)
lign1 = Eq(Kb, (x * x) / (konc - x))
pOH = -math.log10(solve(lign1)[1])
pH = 14 - pOH
# print(pH)

## ## ##
# 15 g natriumacetat (CH3COONa) opløses i 200 ml vand. pKa for eddikesyre er 4,8. 
# Hvad er pH i opløsningen når ligevægten har indstillet sig?
molarmasse = 2 * 12.011 + 3 * 1.008 + 2 * 16 + 22.99
stofmængde = 15/molarmasse
stofmængde *= 5
pkb = 14 - 4.8
Kb = 10**(-pkb)
lign1 = Eq(Kb, (x * x) / (stofmængde - x))
pOH = -math.log10(solve(lign1)[1])
pH = 14 - pOH
# print(pH)

## ## ## 
# En kemiker laver en pufferblanding ved at blande eddikesyre (CH3COOH, pKa = 4,756) med natriumacetat (CH3COONa), 
# således at koncentrationerne bliver:
# [CH3COOH] = 0,3 M
# [CH3COO-] = 0,5 M
# Hvad er pH i opløsningen?
pKa = 4.756
pH = pKa + math.log10(0.5/0.3)
# print(pH)

## ## ##
# En kemiker laver en pufferblanding ved at opløse 10 g natriumacetat (CH3COONa) i 100 ml, 
# 2 M eddikesyre (CH3COOH, pKa = 4,756).
molarmasse = 2 * 12.011 + 3 * 1.008 + 2 * 16 + 22.99
stofmængde = 10/molarmasse
stofmængde *= 10 # sådan at vi har antal mol / liter, da det ellers var mol / 100 ml
pKa = 4.756
pH = pKa + math.log10(stofmængde/2)
# print(pH)

## ## ##
# En kemiker laver en pufferblanding ved at opløse 0,065 g NaHEPES (MW = 260,3 g/mol, pKa = 7,5) i vand, 
# tilsætte 0,19 ml, 1 M HCl og fylde op med vand så det samlede volumen bliver 50 ml.
# Hvad er pH i opløsningen?
molarmasse = 260.3
stofmængde_i_alt = 0.065/molarmasse
pKa = 7.5
syre_stofmængde = 1 * 0.19 * 10 ** -3
stofmængde_tilbage = stofmængde_i_alt - syre_stofmængde
# print(stofmængde, syre_stofmængde)
pH = pKa + math.log10(stofmængde_tilbage/syre_stofmængde)
# print(pH)

## ## ##
# Beregn opløseligheden af Cu(OH)2 i g/L
# Ksp = 2.2 * 10-22
# 1 Cu(OH)2 giver 1 Cu og 2 OH
# Dermed: Ksp = (s)(2s)^2 = 4s^3
Ksp = 2.2 * 10**-22
lign1 = Eq(Ksp, 4*x**3)
# print(solve(lign1))

## ## ##
# Der opløses 10 g NaCl i 200 ml vand. Opløselighedsproduktet for NaCl er 36. Er opløsningen umættet eller overmættet?
Ksp = 36
molarmasse = 22.99 + 35.45
stofmængde = 10/molarmasse
stofmængde *= 5
Q = stofmængde * stofmængde
# print(Q, Ksp)

## ## ## 
# Opløselighedsproduktet for CaCO3 er Ksp = 8,7 · 10-9. Beregn den molære opløselighed.
Ksp = 8.7 * 10**(-9)
lign1 = Eq(Ksp, x * x)
# print(solve(lign1)[1], "M, mol/liter")

## QUIZ ## 
# 1. 
pOH = -math.log10(3.5*10**-5)
pH = 14 - pOH
# print(pH)

# 4. 1.2 gram NaOH opløses i 3 liter vand. Hvad bliver pH?

# print(-math.log10(1.7*10**-4))

# 1. En 1-liters opløsning fremstilles ved at blande 0.5L 0.2 M saltsyre (HCl) 
# og 0.5L 0.4M salpetersyre (HNO3). Til denne opløsning tilsættes 0.29 mol NaOH.
# Angiv pH af den resulterende opløsning (volumenet er stadig 1L).

# HUSK: c1 * v1 = c2 * v2, så bare finde den man mangler
c_HCl = 0.2 * 0.5 / 1
c_HNO = 0.4 * 0.5 / 1
c_h_plus = c_HCl + c_HNO
c_NaOH = 0.29
c_h_plus_efter = c_h_plus - c_NaOH
pH = -math.log10(c_h_plus_efter)
# print(pH)

# 2.
# Antag, at yderligere deprotonering ikke finder sted i sodavanden. [H3O+] måles ved titrering til at være 0.003 M.
# Angiv pH i sodavanden.
ph = -math.log10(0.003)
# print(ph)

# 3.
# Udregn koncentrationen af hydroxidion, [OH-], i en vandig opløsning med pH = 6.39.
pOH = 14 - 6.39
konc = 10**(-pOH)
# print(konc)

# 4.
# Hvad er pH i 1 liter opløsning af 0.25 mol ammoniak i vand? (Kb for NH3 = 1.8 · 10-5)
stofmængde = 0.25
Kb = 1.8 * 10**-5
lign1 = Eq(Kb, (x * x) / (stofmængde - x))
pOH = -math.log10(solve(lign1)[1])
pH = 14 - pOH
# print(pH)

# 5.
# Udregn opløseligheden af Ca3(PO4)2 ved 25 °C. Opløselighedsproduktet for Ca3(PO4)2 er Ksp = 1,3 · 10-32 ved denne temperatur. 
# Der ses bort fra fosfationernes basiske egenskaber.
Ksp = 1.3 * 10**-32
lign1 = Eq(Ksp, (3*x)**3 * (2*x)**2)
# print(solve(lign1))
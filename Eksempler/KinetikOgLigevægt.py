## ## ##
# En reaktions sker som følger: 2 A + B -> C + D
#1: 0,01 M/s = k · 1x · 0,5y
#2: 0,04 M/s = k · 2x · 0,5y
#3: 0,08 M/s = k · 2x · 1y

# finder x: 0,01 M/s / 0,04 M/s= k · 1x · 0,5y / k · 2x · 0,5y = (1/2)^x
# dermed skal x = 2

# 0,08 M/s / 0,04 M/s = k · 2x · 1y / k · 2x · 0,5y = (1/0.5)^y
# dermed skal y = 1

# Dermed reaktionsorden = 3

## ## ##
# Sulfurylchlorid nedbrydes til svovldioxid og chlorgas i en lukket beholder ved følgende førsteordens reaktion 
# med en hastighedskonstant på 4,3 · 10-4 s-1.
# Hvis startkoncentrationen af sulfurylchlorid er 0,2 M, hvad er koncentrationen så efter 5 minutter?
k = 4.3 * 10**(-4)
# Vi kender følgende sammenhæng for førsteordensreaktioner: ln[A]_t = -k*t + ln[A]_0
import math
A_300 = math.exp(-k*300 + math.log(0.2))
# print(A_300)

## ## ##
# Sulfurylchlorid nedbrydes til svovldioxid og chlorgas i en lukket beholder ved følgende førsteordens reaktion 
# med en hastighedskonstant på 4,3 · 10-4 s-1.
# Hvis startkoncentrationen af sulfurylchlorid er 0,2 M, hvor lang tid går der før 60% er nedbrudt?
from sympy import *
x = symbols("x")
k = 4.3 * 10**(-4)
slut_koncentration = 0.2 * 0.4
lign1 = Eq(math.log(slut_koncentration), -k*x + math.log(0.2))
# print(solve(lign1))

## ## ##
# Ved en anden temperatur bestemmes hastighedskonstanten for nedbrydningen af sulfurylchlorid til 6,9 · 10-4 s-1.
# Hvor lang tid går der før halvdelen af sulfurylchloridet er nedbrudt?
k = 6.9 * 10**(-4)
slut_koncentration = 0.2 * 0.5
lign1 = Eq(math.log(slut_koncentration), -k*x + math.log(0.2))
# print(solve(lign1))

## ## ## 
# For andenordensreaktioner vil x = 2, aldrig x = y = 1
# Kombinationen af iodatomer til iodmolekyler er en andenordens reaktion med en hastighedskonstant på 9,3 · 10^8 M-1 s-1.
# Hvis startkoncentrationen af I er 5,1 · 10-3 M, hvad er koncentrationen så efter 5 minutter?
# For andenordens gælder:
# 1/A_t = k*t + 1/A_0
A_0 = 5.1 * 10**-3
k = 9.3 * 10**8
t = 5 * 60
A_300 = 1 / (k*t + 1/A_0)
# print(A_300)

## ## ##
# Hastighedskonstanten for en andenordens reaktion måles ved 10 °C til 4,8 · 10-4 M-1 · s-1, 
# og ved 30 °C til 3,3 · 10-3 M-1 · s-1. Hvad er aktiveringsenergien for denne reaktion?
# ln(k1/k2) = Ea / R * (T1-T2) / (T1*T2)
# Ea = ln(k1/k2) * (T1*T2) / (T1-T2) * R
R = 8.314
T1 = 10 + 273.15
T2 = 30 + 273.15
k1 = 4.8 * 10**-4
k2 = 3.3 * 10**-3
Ea = math.log(k1/k2) * ((T1*T2) / (T1-T2)) * R
# print(Ea, "J/mol")
# print(Ea/1000, "kJ/mol")

## ## ## 
# Hastighedskonstanten for en førsteordens reaktion måles ved 25 °C til 1,9 · 10-5 s-1. 
# Hvis aktiveringsenergien er 30 kJ/mol, hvad er så hastighedskonstanten ved 100 °C?
import numpy as np
from decimal import Decimal
from mpmath import mp
R = 8.314
T1 = 25 + 273.15
T2 = 100 + 273.15
k1 = 1.9 * 10**-5
Ea = 30*1000 # J/mol

lign1 = Eq(k1/x, math.exp(Ea / R * ((T1-T2) / (T1*T2))))
k2 = k1 / np.exp(Ea / R * ((T1-T2) / (T1*T2)))
# print(solve(lign1), "s^(-1)")
# print(k2, "s^(-1)")

## ## ## LIGEVÆGT
# p(N2(g)) = 0,20 atm
# p(H2(g)) = 0,60 atm
# p(NH3(g)) = 0,10 atm
# ligevægtskonstanten ved 300 °C er bestemt til 2,8 · 105
# Beregn reaktionskvotienten Q, og bestem hvilken retning reaktionen forløber i fra begyndelsen.
# N2 + 3H2 <-> 2 NH3
q = 0.10**2 / (0.2**1 * 0.6**3 )
# print(q)
# Da q er lavere en k, så vil der dannes mere produkt

## ## ##
# Ligevægtskonstanten for følgende reaktion er ved 25 °C bestemt til 1,01 · 10-2:
# Ved ligevægt måles partialtrykket af hydrogengas til 0,21 atm og partialtrykket af chlorgas til 0,46 atm. 
# Beregn partialtrykket af hydrogenchlorid.
# H2 + Cl2 <-> 2HCl
k = 1.01 * 10**-2
tryk_hcl = sqrt(k * 0.21 * 0.46)
# print(tryk_hcl) # atm

## QUIZ ## 
# 1.
k = 3 * 10**-3
T = 298 # K
# Bruger: 1/A_t = k*t + 1/A_0
lign1 = Eq(1 / (0.5 * 0.5), k * x + 1 / 0.5)
# print(solve(lign1))

# 2.
k = 0.01
T = 37 + 273.15
c = 0.2 / 5 # mol / liter
lign1 = Eq(1 / (c * 0.5), k * x + 1 / c)
# print(solve(lign1))

# 3. 
k = 3.7 * 10**-2 # s-1
T = 150 + 273.15 # K
Ea = 71 * 1000 # J/mol
# Bruger: k = A * exp(-E_a / (R*T))
lign1 = Eq(k, x * math.exp(-Ea / (R*T)))
A = solve(lign1)[0]
T = T = 170 + 273.15 # K
nye_k = A * math.exp(-Ea / (R*T))
# print(nye_k)

# 4.
k = 0.02 #s-1
T = 680 + 273.15 # K
c = 1
c_slut = 0.125
halveringstid = math.log(2) / k # sec
# 1 / 2 -> 0.5 / 2 -> 0.25 / 2 -> 0.125 
# dermed blot gange med 3
# print(halveringstid * 3, "sek")

# 1. 
# hastighed = k * []^n

# 2.
# plot, find værdier: y = ax + b 
# a = k
# A_0 er givet i opgaven
# t_1/2 = 1 / (k * [A]_0)


# 4.
A = 0.1
B = 0.2
C = 0.4
k = (B**2 * C**1) / (A**3)
print(k)

# 5.
NOBr = 0.1
NO = 0.2
Br = 0.1
q = (NO**2 * Br) / NOBr**2
print(q)
k = 0.064
# Da q er større end k vil den løbe mod reaktantsiden (venstre)

# 3.
k = 10
T = 298 # K
A = 10**8
# find Ea
# bruger: k = A * exp(-E_a / (R*T))
Ea = -R*T*math.log(k/A)
print(Ea, "J")
Na = 6.02 * 10**23 # Avogadros konstant
h = 6.626 * 10**-34 # Plancks konstant
v = Ea / (Na * h)
print(v)

# 4.
k = 4.2
nitrogen = 0.2
hydrogen = nitrogen * 3 # da forholdet er 1:3
ammoniak = x - 2 * nitrogen # da forholdt er 2:1
# dermed kan ukendt findes
lign1 = Eq(k, ammoniak**2/(nitrogen**1*hydrogen**3))
# print(solve(lign1))

# 5
t_halv = 5730
A_t = 2.3
A_0 = 15.3
t = -t_halv/math.log(2) * math.log(A_t/A_0)
print(t, "år")
print(5730 * 2.7)

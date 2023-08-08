## Celcius til kelvin:
# 0 C = 273.15 K

## ## ##
# 93.4 g svovldioxid oxideres fuldstændigt. Hvor meget varme udvikles der?
# 2 SO_2 + O_2 -> 2 SO_3
# DeltaH = -198.2 kJ/mol

# Først: For hvert mol svovldioxid dannes kun den halve mængde, da 2 i reaktionen
# DeltaH = -99.1 kJ/mol
# Molarmasse SO_2 = 64.07 g/mol
# Stofmængde = find_stofmængde(93.4, 64.07)
# final_deltaH = DeltaH * Stofmængde

## ## ##
# Standard reaktionsentalpien for denne reaktion:
# H+ + OH- -> H2O (l)
# Finder relevante konstanter i appendix 2
# DeltaH = -285.8 - (-229.94 - 0)

## ## ##
# Ved hvilke temperaturer er en reaktion med følgende værdier spontan?
# DeltaH = 5.4 kJ/mol
# DeltaS = 18 J/(mol * K)
# DeltaH = 5400 J/mol
# Skilletemperatur = DeltaH / DeltaS = 300
# Dermed skal temperaturen > 300

## ## ## 
# En ligevægtskonstant er ved 800 C
# K = 2.5 * 10**(-3)
# R = 8.314
# T = 800 + 273.15
# DeltaG = -R*T*math.log(K)
# # Enhed: J * mol-1

## ## ##
# Find ligevægtskonstanten ved 25 C for:
# 2 SO_2 + O_2 -> 2 SO_3
# produkter = 2 * -370.4
# reaktanter = 2 * -300.4 - 0
# DeltaH = produkter - reaktanter
# import math
# final = math.exp(-DeltaH*1000/(8.314 * (25 + 273.15)))
# print(final)

## CODE ##

produkter = 2 * -370.4
reaktanter = 2 * -300.4 - 0
DeltaH = produkter - reaktanter



### QUIZ 1
# 1
## Code 
BaCo3 = -823 + -393.5
BaO = -1107/2

produkter = BaO - 393.5
reaktanter = BaCo3
DeltaH = produkter - reaktanter
print(DeltaH)

# 2
## Code 
stofmængde = 100/(24.305 + 2 * 15.999 + 2 * 1.008)
produkter = -462 + 2 * -229.9
reaktanter = -924.7
DeltaH = produkter - reaktanter
print(DeltaH*stofmængde)

# 3
## Code
produkter = -2 * 16.6
reaktanter = 0
DeltaH = produkter - reaktanter
import math
print(math.exp(-DeltaH*1000/(8.314 * (25 + 273.15))))

# 4
## Code
produkter = 193
reaktanter = 2 * 248.5 + 205
DeltaH = produkter - reaktanter
print(DeltaH)

### QUIZ 2:
# 1
## Code
gram = 100 * 0.7138
stofmængde = gram / (4 * 12.011 + 10 * 1.008 + 15.999)
print(stofmængde * 26.5)

# 2
## Code
br = (0.03**2 * 6.4 * 10**(-2)) / 0.03**2
print(br)

# K = [C]^c*[D]^d / [A]^a*[B]^b
# 6.4 * 10**(-2) = 0.03**2 * X / 0.03**2

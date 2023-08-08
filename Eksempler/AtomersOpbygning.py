## ## ##
# Hvad er frekvensen af lys med en bølgelængde på 300 nm?
lys_hastighed = 3 * 10**8 # m / s
bølgelængde = 300 * 10**(-9) # m
frekvens = lys_hastighed / bølgelængde
print(frekvens)

## ## ##
# Hvad er energien af lysfotoner med en frekvens på 2,4 GHz
planks_konstant = 6.63 * 10**(-34) # J*s
frekvens = 2.4 * 10**(9) # Hz
energi = planks_konstant * frekvens
print(energi)

## ## ## 
# Hvad er energien af en lysfoton med bølgelængden 1 Å?
# 1 Å = 10**(-10) m
planks_konstant = 6.63 * 10**(-34) # J*s
lys_hastighed = 3 * 10**8 # m / s
bølgelængde = 1 * 10**(-10) # m
energi = planks_konstant * lys_hastighed / bølgelængde
print(energi)

## ## ##
# Der udsendes en energi på 4,30 * 10**(-19) J. Hvilken farve har fotonerne?
planks_konstant = 6.63 * 10**(-34) # J*s
lys_hastighed = 3 * 10**8 # m / s
energi = 4.30 * 10**(-19)
bølgelængde = planks_konstant * lys_hastighed / energi
print(bølgelængde)
print(bølgelængde * 10**9, "nm")

## ## ##
# Fulde, ikke forkotede elektronkonfiguration for 1. carbon og 2 . klor:
# Carbon = 1s^2 2s^2 2p^2
# Klor = 1s^2 2s^2 2p^6 2 3s^2 3p^5
# Forkotet version af Al: [Ne]3s^2 3p^1
# Nikkel = 1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^8 = [Ar] 4s^2 3d^8
# S^(-2) = [Ar] = 1s^2 2s^2 2p^6 3s^2 3p^6

## QUIZ ##
# 1: Bølgelænde er 15 cm. 4.184 J er nødvendigt for at øge 1 g vand med 1 C.
#  Hvor mange fotoner kræves for 350 mL vand fra 20 til 95 C
energi = 4.184 # J
alt_energi_nødvendigt = energi * 350 * (95 - 20)
bølgelængde = 15 * 10**(-2)
energi_pr_foton = planks_konstant * lys_hastighed / bølgelængde
print(alt_energi_nødvendigt / energi_pr_foton)

# 2: ioniseringsenergi for gasformig sølv Ag(g) er 7,58 eV (= 727 kJ/mol)
# Angiv den bølgelængde af lys, der lige netop kan ionisere sølv-atomet til Ag+.
planks_konstant = 4.13 * 10**(-15) # eV*s
energi = 7.58 # eV
bølgelængde = planks_konstant * lys_hastighed / energi
print(bølgelængde)

# 1: Hvor mange elektroner er der i alt (ikke kun valenselektroner) i a) CH3 CH2 OH, b) MnO_4-, og c) Ag+?
# Tæller blot antallet i hvert atom: 26, 58 og 46

# 2: Hvor mange elektroner sidder i p-orbitaler i hhv. a) et kobber-atom, b) sølv-atom og c) guld-atom?
# Copper: 29: 1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^9 = 12
# Sølv: 47: 1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^10 4p^6 5s^2 4d^9 = 18
# Guld: 79 = 24



import math
## ## ##
# Hvad er standardcellepotentialet for denne reaktion:
# I2 + SO2 + 2H2O -> 2I- + SO4 2- + 4H+
# Katode: I2 + 2e -> 2I-                    : 0.53
# Anode: SO4 2- + 4H+ + 2e -> SO2 + 2H2O    : 0.2
total = 0.53 - 0.2
print(total)

## ## ##
# Standardcellepotentialet (Eocelle) for nedenstående reaktion er målt til +0.29 V.
# Sn + 2Cu2+ <-> Sn2+ + 2Cu+
# Delta gibbs = -n*F*E_celle
E_celle = 0.29
F = 96500 # C/mol
n = 2 # Molantallet af elektroner der overføres kan findes ved at finde op og nedgange i oxidationstal og gange med molkvotienterne.
gibbs = -n*F*E_celle # J / mol
print(gibbs/1000, "kJ/mol")

## ## ##
# Standardcellepotentialet (Eocelle) for nedenstående reaktion er målt til +0.65 V.
# Cr2O7 2- + 3H2O2 + 8H+ -> 2Cr3+ + 3O2 + 7H20
# Find gibbs
E_celle = 0.65
F = 96500 # C/mol
n = 6

# Molantallet af elektroner der overføres kan findes ved at finde op og nedgange i oxidationstal og gange med molkvotienterne. 
# Oxidationstallet for chrom er +6 før og +3 efter. For oxygen er det -1 før og 0 efter. 
# Da der er to chromatomer og seks oxygenatomer må der overføres 6 elektroner i reaktionen: 
# hvert oxygenatom afgiver én elektron, og hvert chromatom optager tre. 

gibbs = -n*F*E_celle # J / mol
print(gibbs/1000, "kJ/mol")

## ## ##
# Mg + I2 <-> Mg2+ + 2I-
katode = 0.53
anode = -2.37
total = katode - anode
F = 96500 # C/mol
n = 2
gibbs = -n*F*total # J / mol
R = 8.314 # J / (K * mol)
T = 25 + 273 # K # 273.15 giver åbenbart ikke rigtigt??
print(gibbs, R, T)
# DeltaG = -R*T*ln(K)
K = math.exp(-gibbs/(R*T))
print(K)

# Br2 + Pb <-> 2Br- + Pb2+
katode = 1.07
anode = -0.13
total = katode - anode
F = 96500 # C/mol
n = 2
gibbs = -n*F*total # J / mol
R = 8.314 # J / (K * mol)
T = 25 + 273 # K # 273.15 giver åbenbart ikke rigtigt??
print(gibbs, R, T)
# DeltaG = -R*T*ln(K)
K = math.exp(-gibbs/(R*T))
print(K)

## ## ##
# Beregn E for følgende reaktion:
# Mg + Sn2+ <-> Mg2+ + Sn
#[Mg2+] = 0.045 M, [Sn2+] = 0.035
# Bruger: E = E0 - R*T/(n*F) * ln(Q)
katode = -0.14
anode = -2.37
E0 = katode - anode
Q = 0.045/0.035
n = 2
R = 8.314 # J / (K * mol)

E = E0 - R*T/(n*F) * math.log(Q)
print(E)


## QUIZ ##
# 3.
E_celle = 3.1
F = 96500 # C/mol
n = 2 # Molantallet af elektroner der overføres kan findes ved at finde op og nedgange i oxidationstal og gange med molkvotienterne.
gibbs = -n*F*E_celle # J / mol
print(gibbs/1000, "kJ/mol")

# 6.
katode = 0.8
anode = -0.25
E0 = katode - anode
T = 298.15
Q = 0.3/2**2
n = 2
R = 8.314 # J / (K * mol)

E = E0 - R*T/(n*F) * math.log(Q)
print(E)


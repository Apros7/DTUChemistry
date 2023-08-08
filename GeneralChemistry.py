
######################
## HELPER-FUNCTIONS ##
######################

def find_molarmasse(*args):
    # input needs to be infinite number of tuples with 1) molarmass and 2) number of atoms
    return sum([arg[0]*arg[1] for arg in args])

def find_stofmængde(molarmasse, m = 1000):
    # g / (g / mol) = mol
    # m skal angives i gram
    return m / molarmasse

def empirisk_formel(analysemål: list, molarmasser: list):
    # analysemål is list of procent from analyse: eg. 52.2, 13.1, 34.7
    stofmængder = [find_stofmængde(molar, a) for a, molar in zip(analysemål, molarmasser)]
    return [stof / min(stofmængder) for stof in stofmængder]

def mol_til_antal(tal):
    return tal * 6.022 * 10**(23)

######################
## QUESTION FOMULAS ##
######################

def masseprocent_af_atom_i_stof(atomer: list, molarmasser: list, atom_index: int):
    ## INPUTS ##
    # 1. Tæl antallet af de forskellige atomer
    # 2. Find de tilhørende molarmasser
    # Atomindex er index på det atom, som der skal findes masseprocent af
    stof_molarmasse = sum([atom * molarmasse for atom, molarmasse in zip(atomer, molarmasser)])
    atom_molarmasse = atomer[atom_index] * molarmasser[atom_index]
    return atom_molarmasse / stof_molarmasse

def antal_atomer_i_stof(stof_molarmasse, antal_af_atom_i_stof, vægt_tal):
    # Find først molarmasse for hele stoffet
    # Angiv hvor mange atomer i stoffet samt vægt (eks. 7 gram)
    stofmængde = find_stofmængde(stof_molarmasse, vægt_tal)
    antal_atomer = mol_til_antal(stofmængde)
    return antal_atomer * antal_af_atom_i_stof

def hvor_meget_atom_dannes(molmængder: list, stof_molarmasse: float, atom_til_stof_ratio: int):
    pass

## BEREGNINGER ##
cl_molarmasse = 35.45
ag_molarmasse = 107.8682
cl_stofmængde = 2 * 0.005
ag_stofmængde = 1 * 0.1
## forholdet er 1:1, derfor
AgCl_stofmængde = cl_stofmængde
AgCl_molarmasse = cl_molarmasse + ag_molarmasse
AgCl_mass = AgCl_molarmasse * AgCl_stofmængde
# print(AgCl_mass) # g

## BEREGNINGER ##
N_vægt = 6
brint_vægt = 0.5
N_molarmasse = 28
H_molarmasse = 2
N_stofmængde = find_stofmængde(N_molarmasse, N_vægt)
H_stofmængde = find_stofmængde(H_molarmasse, brint_vægt)
am_mol = 2*H_stofmængde/3
am_molarmasse = 14 + 3*1
# print(am_mol*am_molarmasse)

# BEREGNINGER ##
liter_oktan = 15000/14 # liter
oktan_massefylde = 0.91 # kg/liter
oktan_kg = liter_oktan * oktan_massefylde
oktan_molarmasse = 8*12.011 + 18*1.008
oktan_mol = find_stofmængde(oktan_molarmasse, oktan_kg)
co2_mol = 8*oktan_mol
co2_molarmasse = 12.011 + 2 * 15.999
co2_kg = co2_mol * co2_molarmasse
#print(co2_kg)

## BEREGNINGER ##
# print(find_stofmængde(14 + 3, 10))
# print(find_stofmængde(32, 20))

mass = find_stofmængde(14 + 3, 10)
molarmasse = 14 + 16
# print(mass*molarmasse)

############
## GASSER ##
############

# Find Volumen
V = 10 * 0.0821 * (20 + 273.15) / 1
#print(f"{V = }")

# Find stofmængde:
grader_celcius = 25
p = 1 # atm
R = 0.081
V = 4 # L
T = (grader_celcius + 273.15) # K
n = p * V / (R * T)
print(f"{n = }")

# Find tryk
mol_co2 = find_stofmængde(32 + 12, 10) + n
grader_celcius = 25
volumen_liter = 1/2
p = mol_co2 * 0.0821 * (grader_celcius + 273.15) / volumen_liter
#print(f"{p = }")

# Find temp
V = 10000 # L
R = 0.0821 # L * mol-1 * bar * K-1
n = find_stofmængde(12 + 4, 1000000) # mol
p = 200 # atm
T = p * V / (n * R)
print(f"{T = } K")
T -= 273.15
print(f"{T = } C")

# Find molbrøker
Pi = 0.28
Ptotal = 0.28 + 0.4 + 0.11
molbrøk = Pi / Ptotal
# print(f"{molbrøk = }")


##############
## FORMULAS ##
##############

# IDEALGASLOVEN
# p * V = n * R * T
# R = 0.0821 L amt/(K mol)        # Brug ved ATM
# eller R = 8.314 J/(mol * K)     # Brug ved bar

# Kan omskrives til: M = rho*R*T/p
# Kan bruges til at finde molær (g/mol) for en ukendt gas i kendt rum. Rho skal være g/L

# Ikke- IDEALGAS
# Van der Waals Ligning:
# (p + an^2 / V^2) (V - nb) = nRT
# a and b can be found in book

# Daltons lov
# Pt = P1 + P2
# Det totale tryk er summen af de individuelle partialtryk
# Pi = Xi * Pt
# Partialtrykket kan udregnes ud fra totaltrykket og molfraktionen


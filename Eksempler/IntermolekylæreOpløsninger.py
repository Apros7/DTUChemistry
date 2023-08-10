# Eksempler med molaritet eller molalitet

## ## ##
# Densitet rødvin: 0.902 g/ml. Koncentration ethanol 5 M, molarmasse ethanol 32.04 g/mol. Hvad er molaliteten
# Molaliteten er molmængden af soluten (ethanol) per kilogram opløsningsmiddel (vand)
# Vi tager udgangspunkt i 1 liter, derfor bliver g / L -> g
masse_ethanol = 5 * 32.04 # g 
masse_ethanol_og_vand = 0.902 * 1000 # g 
masse_vand = masse_ethanol_og_vand - masse_ethanol # g
masse_vand_kg = masse_vand / 1000 # kg
molalitet = 5 / masse_vand_kg
print(molalitet, "m")

## ## ##
# Hvad er molaliteten af en 30% (w/w) (vægt per vægt) opløsning af HCl?
# Dermed 300 g HCl per 1 kg opløsning. Dermed 700 g vand.
hcl_molarmasse = 35.45 + 1.008 # g/mol
mol_hcl = 300 / hcl_molarmasse
masse_vand_kg = 0.7 # kg
molalitet = mol_hcl / masse_vand_kg
print(molalitet, "m")

## ## ##
# kogepunktsforøgelseskonstan, kb = 1.13 C / m. Hvad bliver ændringen af kogenpunktet for en 5.13 m opløsning?
# bruger: DeltaTb = Kb*m
kogepunktsforøgelse = 1.13 * 5.13 # C
print(kogepunktsforøgelse, "C")

## ## ##
# 15 sukker opløses i 100 ml vand. Hvad er kogepunktet for opløsningen?
# 100 ml vand = 100 g vand
molarmasse_sukker = 12 * 12.011 + 22 * 1.008 + 11 * 15.999 # g/mol
molar = 15 / molarmasse_sukker # mol
molalitet = molar / 0.1 # skal være i kg, derfor 0.1 kg
konstant = 0.51 # C / m
kogepunktsforøgelse = konstant * molalitet # C
kogepunkt = 100 + kogepunktsforøgelse
print(kogepunkt, "C")

## ## ##
# 87 enthylenglycol (C2 H6 O2) opløses i 300 ml vand. Hvad er frysepunktet for opløsning?
# 300 ml vand = 300 g vand
molarmasse = 2 * 12.011 + 6 * 1.008 + 2 * 15.999 # g/mol
molar = 87 / molarmasse
molalitet = molar / 0.3
konstant = 1.86 # C / m
frysepunktsforøgelse = konstant * molalitet
frysepunkt = 0 - frysepunktsforøgelse
print(frysepunkt, "C")

## ## ##
# I en celle er der opløst 9.1 mg glukose (c6 h12 o6) i 3 ml vand ved 37 C. Beregn det osmotiske tryk for opløsningen.
# pi = M*R*T
T = 37 + 273.15 # K
R = 0.0821 # L * mol-1 * bar * K-1
molarmasse = 6 * 12.011 + 12 * 1.008 + 6 * 15.999 # g/mol
M = ((9.1 /1000) / molarmasse) / 0.003
tryk = M * R * T # bar
print(tryk, "atm")

## ## ## 
# 30 g NaCl opløses i 100 ml vand. Hvad er kogepunktet for opløsningen?
molarmasse_sukker = 22.99 + 35.45 # g/mol
molar = 30 / molarmasse_sukker # mol
molalitet = molar / 0.1 # skal være i kg, derfor 0.1 kg
konstant = 0.51 # C / m
kogepunktsforøgelse = konstant * molalitet # C
# Husk Van't Hoff faktor: antal partikler pr. partikel tilsæt. I dette tilfælde 2, da Na+ og Cl-
kogepunktsforøgelse *= 2
kogepunkt = 100 + kogepunktsforøgelse
print(kogepunkt, "C")

## ## ##
# 87 g MgCl2 opløses i 90 ml vand. Hvad er frysepunktet for opløsningen
molarmasse = 24.305 + 2 * 35.45 # g/mol
molar = 87 / molarmasse
molalitet = molar / 0.09
konstant = 1.86 # C / m
frysepunktsforøgelse = konstant * molalitet
# Husk Van't Hoff faktor: antal partikler pr. partikel tilsæt. I dette tilfælde 3, da Mg2+ og 2Cl-
frysepunktsforøgelse *= 3
frysepunkt = 0 - frysepunktsforøgelse
print(frysepunkt, "C")

## ## ##
# 15 mg Na2 HPO4 opløses i 5 ml vand ved 20 °C. Beregn det osmotiske tryk for opløsningen.
T = 20 + 273.15 # K
R = 0.0821 # L * mol-1 * bar * K-1
molarmasse = 2 * 22.99 + 1 * 1.008 + 4 * 15.999 + 1 * 30.9737# g/mol
M = ((15 /1000) / molarmasse) / 0.005
tryk = M * R * T # bar
# Husk Van't Hoff faktor: antal partikler pr. partikel tilsæt. I dette tilfælde 3, da 2Na+ og HPO4 2-
tryk *= 3
print(tryk, "atm")


## QUIZ ##
# 1. 
# 5 g ukendt til 250 g napthalen. Kogepunkt forøges med 0.652. Hvor stor er molære masse af ukendt, hvis Kb = 5.803?
molalitet = 0.652 / 5.803
molar = molalitet * 0.25
molarmasse = 5 / molar
print(molarmasse, "g/mol")

# 2. 
# En frø benytter glucose (C6H12O6) som antifrostvæske om vinteren. Hvis frøens celler indeholder 60 gram glucose 
# pr. 200 mL cellevæske, og cellevæsken vejer 1 g/mL, hvad bliver så frysepunktssænkningen i den pågældende frø? 
# Benyt, at Kf = 1,86 °C kg/mol
molarmasse = 6 * 12.011 + 12 * 1.008 + 6 * 15.999 # g/mol
molar = 60 / molarmasse
molalitet = molar / 0.2
konstant = 1.86 # C / m
frysepunktsforøgelse = konstant * molalitet
# Husk Van't Hoff faktor: antal partikler pr. partikel tilsæt. I dette tilfælde 3, da Mg2+ og 2Cl-
frysepunktsforøgelse *= 1
frysepunkt = 0 - frysepunktsforøgelse
print(frysepunkt, "C")

# 4. 
# En 111 mg prøve af Eugenol opløses i 1,00 g chloroform (Kb = 3,63 °C/m), hvorved kogepunktet af chloroform hæves med 2,45 °C. 
# Hvor stor er den molære masse, M, af Eugenol?
frysepunktsforøgelse = 2.45
konstant = 3.63
molalitet = frysepunktsforøgelse / konstant
molalitet *= 0.001
molarmasse = (111 / 1000) / molalitet
print(molarmasse, "g/mol")

## QUIZ 2 ##
# 1 gram af et stof tilsat til en 100 gram opløsning observeres at sænke frysepunktet med -0.5˚C. 
# Opløsningen har Kf = 5.0 °C/m og Van't Hoff faktoren i = 1. Opløsningen har densiteten 1 g/mL.
# Angiv molmassen af stoffet.

frysepunktsforøgelse = 0.5
konstant = 5
molalitet = (frysepunktsforøgelse / konstant) * 0.1 # kg
masse = 1 # g
molarmasse = masse / molalitet
print(molarmasse, "g/mol")

# 2. Test forskellige stoffer for størst frysepunktsænkning
molalitet_og_vant_hoff_faktor = [
    (2, 4), (3, 1), (2, 3), (3, 1), (2, 2)
]
print("Test af frysepunktssænkning")
for molalitet, vant_hoff_faktor in molalitet_og_vant_hoff_faktor:
    konstant = 0.51 # C / m
    kogepunktsforøgelse = konstant * molalitet # C
    # Husk Van't Hoff faktor: antal partikler pr. partikel tilsæt. I dette tilfælde 2, da Na+ og Cl-
    kogepunktsforøgelse *= vant_hoff_faktor
    kogepunkt = 100 + kogepunktsforøgelse
    print(kogepunkt, "C")

# 3. 
# 10 gram af et protein opløses i vand, så det samlede volumen er 1 L. 
# Det osmotiske tryk for denne protein-opløsning måles at være 0,0075 atm ved 25°C. 
# Proteinet består af i alt 306 aminosyrer. Udregn først molmassen for proteinet, 
# og bestem herudfra den gennemsnitlige molmasse (i gram/mol) af en aminosyre i proteinet.

T = 25 + 273.15 # K
R = 0.0821 # L * mol-1 * bar * K-1
tryk = 0.0075 # bar
M = tryk / (R * T)
molarmasse = (10) / M
molarmasse_pr_aminosyrer = molarmasse / 306
print(molarmasse_pr_aminosyrer, "g/mol")
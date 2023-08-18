correct = 0
## ## ##

# 2.
# E = h*c/lambda
h = 6.626 * 10**(-34) # J*s
c = 3.00 * 10**8 #m/s
E = (418.7 * 1000 - 262.4 * 1000) # J/mol
na = 6.022 * 10**23
lamb = h * c / (E / na)
# print(lamb * 10**7, "nm")
correct += 1

# 3.
correct += 1

import math

# 8.
k_bestemt = [0.011781, 0.30309, 0.52292, 0.74581, 0.095718]
T = [0, 100, 200, 300, 400]
Ea = 8
A = 4
R = 8.3
# formula: k = A * exp(-Ea / (R * T))
# for k_bes, t in zip(k_bestemt, T):
#     print(k_bes)
#     print(A * math.exp(-Ea / (R * (t + 273.15))))
#     print("----")

# 11
vægt = 30
molarmasse = 15.999 + 22.99 + 35.45
stofmængde = vægt / molarmasse
print(stofmængde)

# 12




## ## ## 
print("-------------------")
print(f"{correct}/{20} correct = {round(correct*100/20, 2)}%")
# Code that uses the atom_helper.py module to determine the energy minimum of a Lennard-Jones potential given a set of atomic coordinates

import numpy as np
import matplotlib.pyplot as plt
import atom_helper as ah

atom1 = np.array([2, 3, 4])
atom2 = np.array([3, 1, 2])
distance = ah.distance(atom1, atom2)
print("The distance between atom 1 and atom 2 = {:.2f}".format(distance))

A = float(input("What is A in eVA^12 ? "))
B = float(input("What is B in eVA^6 ? "))
r = float(input("What is r in Angstroms? "))
'''
User input for terms in the Lennard-Jones expression
'''
for i in range (20):
    E = ah.energy_lj(r, A, B)
    Ep = ah.energy_prime(r, A, B)
    Epp = ah.energy_prime_prime(r, A, B)
    print("r = {:.6f} ".format(r), "E = {:.6f} ".format(E), "Ep = {:.6f} ".format(Ep), "Epp = {:.6f} ".format(Epp))
    r1 = r - (Ep/Epp)
    new_E = ah.energy_lj(r1, A, B)
    if new_E>E:
        break
    else:
        r = r1
        
from scipy.optimize import minimize as mz

initial_guess = 4
'''
Uses the minimize function from the scipy library to determine the minimum energy between two atoms given an initial guess. Does not find a global minimum
'''
results = mz(ah.energy_lj, initial_guess, args=(1e5, 40))

print (results)
print()
print(results.x)
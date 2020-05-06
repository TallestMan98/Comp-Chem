import numpy as np
import matplotlib.pyplot as plt
plt.errorbar?

wavenumber_toluene, transmittance_toluene = np.loadtxt('toluene.csv', unpack = True, delimiter = ',')
wavenumber_benzyl, transmittance_benzyl = np.loadtxt('benzyl_alcohol.csv', unpack = True, delimiter = ',')
wavenumber_mixture, transmittance_mixture, uncertainty_mixture = np.loadtxt('mixture.csv', unpack = True, delimiter = ',')
# reading in data from csv files

plt.plot (wavenumber_toluene, transmittance_toluene)
r1,l1 = plt.xlim()
plt.xlim ([l1, r1])
plt.xlabel ("Wavenumber / cm-1")
plt.ylabel ("Transmittance")
plt.title ('Toluene IR')
plt.show()
# pure toluene transmittance plot

plt.plot (wavenumber_benzyl, transmittance_benzyl)
r2,l2 = plt.xlim()
plt.xlim ([l2, r2])
plt.xlabel ("Wavenumber / cm-1")
plt.ylabel ("Transmittance")
plt.title ('Benzyl Alcohol IR')
plt.show()
# pure benzyl alcohol transmittance plot

plt.plot (wavenumber_mixture, transmittance_mixture)
r3,l3 = plt.xlim()
plt.xlim ([l3, r3])
plt.errorbar(wavenumber_mixture, transmittance_mixture, yerr= uncertainty_mixture, xerr=None, fmt = 'None')
plt.xlabel ("Wavenumber / cm-1")
plt.ylabel ("Transmittance")
plt.title ('Experimental IR')
plt.show()
# transmittance plot of unknown mixture

print (np.min(wavenumber_toluene), np.max(wavenumber_toluene))
print (np.min(wavenumber_benzyl), np.max(wavenumber_benzyl))
print (np.min(wavenumber_mixture), np.max(wavenumber_mixture))

optimisation_x = np.copy(wavenumber_mixture)

optimisation_toluene = np.interp(optimisation_x, wavenumber_toluene, transmittance_toluene)

plt.plot (optimisation_x, optimisation_toluene)
r4,l4 = plt.xlim()
plt.xlim ([l4, r4])
plt.xlabel ("Wavenumber / cm-1")
plt.ylabel ("Transmittance")
plt.title ('Interpolated Toluene IR')
plt.show()
# interpolating toluene transmittance data

optimisation_benzyl = np.interp(optimisation_x, wavenumber_benzyl, transmittance_benzyl)

plt.plot (optimisation_x, optimisation_benzyl)
r5,l5 = plt.xlim()
plt.xlim ([l5, r5])
plt.xlabel ("Wavenumber / cm-1")
plt.ylabel ("Transmittance")
plt.title ('Interpolated Benzyl Alcohol IR')
plt.show()
# interpolating benzyl alcohol transmittance data

import benzyl_alcohol_toluene_mixture_functions_module as workshop
t_mixture = workshop.composition_plot(0.5, optimisation_toluene, optimisation_benzyl)
plt.plot (optimisation_x, t_mixture)
r6,l6 = plt.xlim()
plt.xlim ([l6, r6])
plt.xlabel ("Wavenumber / cm-1")
plt.ylabel ("Transmittance")
plt.title ('IR for a mixture of Toluene and Benzyl Alcohol')
plt.show()
# shows a plot of a mixture of toluene and benzyl alcohol given a fractional composition

workshop.goodness_of_fit(0.32253314, optimisation_toluene, optimisation_benzyl, 
                         transmittance_mixture, uncertainty_mixture)
# works out a X^2 value for a fractional composition, compared to our experimental data

from scipy.optimize import minimize
initial_c = 0.5
X2_min = minimize(workshop.goodness_of_fit, initial_c, args = (optimisation_toluene, optimisation_benzyl, 
                                                                   transmittance_mixture, uncertainty_mixture))
# optimised_c = initial_c after the minimization. c is fractional composition
print (X2_min)
# minimisation of the chi squared value so the fractional composition plot best fits the unknown mixture plot

plt.plot (wavenumber_mixture, transmittance_mixture)
plt.plot (optimisation_x, t_mixture_optimised)
r3,l3 = plt.xlim()
plt.xlim ([l3, r3])
plt.errorbar(wavenumber_mixture, transmittance_mixture, yerr= uncertainty_mixture, xerr=None, fmt = 'None')
plt.xlabel ("Wavenumber / cm-1")
plt.ylabel ("Transmittance")
plt.title ('Experimental IR vs optimised c IR')
plt.show()
# plots experimental IR vs IR with optmised c to visualise goodness of fit

accepted_c = []
accepted_X2 = []
for i in range (100):
    X2_new, perturbation = workshop.MCMC (0.5, optimisation_toluene, optimisation_benzyl, 
                         transmittance_mixture, uncertainty_mixture)
print (accepted_c, accepted_X2)
# uses Markov chain Monte Carlo algorithm
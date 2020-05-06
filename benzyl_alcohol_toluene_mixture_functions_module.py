import numpy as np
import matplotlib.pyplot as plt


def composition_plot(c, T1, T2):
    '''
    produces transmittance data for a fractional composition of toluene in a mixture of benzyl alcohol and toluene
    
    Parameters:
        c (float): fractional composition of toluene
        T1 (np.ndarray): interpolated transmittance of toluene
        T2 (np.ndarray): interpolated transmittance of benzyl alcohol
    
    Return:
        np.ndarray: an array of transmittances for a specified fractional composition of toluene
    '''
    t_mixture = c * T1 + (1-c) * T2
    
    if 1 < c < 0:
        raise ValueError ('fraction of toluene cannot be greater than 1 or less than 0')
        
    else: 
        return t_mixture
    

def goodness_of_fit (c, T1, T2, y_exp, dy_exp):
    '''
    Determines the goodness of fit, X^2, of a given set of transmission data for a
    fractional composition, c, of toluene in a mixture of benzyl alcohol and toluene
    
    Parameters:
        T1 (np.ndarray): interpolated transmittance of toluene
        T2 (np.ndarray): interpolated transmittance of benzyl alcohol
        c (float): fractional composition of toluene
        y_exp (np.ndarray): experimental mixture transmittance values
        dy_exp (np.ndarray): uncertainty in experimental transmittance value
    
    Return:
        float: the goodness of fit, the higher the number the worse the fit
    '''
    X2 = np.sum(((composition_plot(c, T1, T2)-y_exp)/dy_exp)**2)
    
    return X2


def MCMC (c, T1, T2, y_exp, dy_exp):
    '''
    Performs Markov chain Monte Carlo algorithm, and returns the updated list
    
    Parameters:
        T1 (np.ndarray): interpolated transmittance of toluene
        T2 (np.ndarray): interpolated transmittance of benzyl alcohol
        c (float): fractional composition of toluene
        y_exp (np.ndarray): experimental mixture transmittance values
        dy_exp (np.ndarray): uncertainty in experimental transmittance value
        
    Return:
        list: updated values of c and X^2
    '''
    accepted_c = []
    accepted_X2 = []
    
    X2_old = goodness_of_fit (c, T1, T2, y_exp, dy_exp)
    
    stepsize = 0.001
    perturbation = stepsize*(np.random.random()-0.5)+c
    
    X2_new = goodness_of_fit (perturbation, T1, T2, y_exp, dy_exp)
    
    probability = np.exp((-X2_new + X2_old)/2)
    
    if probability >= np.random.random():
        accepted_c.append(perturbation)
        accepted_X2.append(X2_new)
        
    return accepted_c, accepted_X2
        

















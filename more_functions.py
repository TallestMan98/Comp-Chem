import numpy as np

# Function for providing the energy of a photon when a wavenumber is provided
from scipy.constants import c, h

def energy(wavenumber):
    '''
    produces energy of photon for a given wavenumber
    
    Parameters:
        wavenumber (float): the wavenumber of the photon
    
    Return:
    float: the energy of the photon
    '''
    energy = h * c * wavenumber
    return energy


# Function for determining the volume of a system using the Ideal Gas Law
from scipy.constants import R

def ideal_gas_law(number_of_moles, temperature, pressure):
    '''
    determines the volume of the gas assuming the gas is ideal, given
    the number of moles of gas, the temperature and the pressure
    
    Parameters:
        number_of_moles (float) = the number of moles of gas
        temperature (float) = the temperature in kelvin
        pressure (float) = the pressure of the system in pascals
    
    Return:
        float: the volume of gas in meters cubed
    '''
    volume = (number_of_moles * R * temperature) / pressure
    
    if temperature < 0:
        raise ValueError ('Temperature cannot be less than 0')
    
    return volume


# Function that returns the allowed values of the angular momentum quantum number, l , given the principal quantum number, n

def allowed_angular_momentum_quantum_numbers(principal_quantum_number):
    '''
    returns the allowed values of the angular momentum quantum number, l
    given the principal quantum number, n
    
    Parameters:
        principal_quantum_number (int) = the given principal quantum number, n
        
    Return:
        list: the possible values of l
        
    '''
    l = []
    if not isinstance (principal_quantum_number, int):
        raise TypeError ('Principal quantum number must be an integer')
    
    if principal_quantum_number <= 0:
        raise ValueError ('Principal quantum number must be greater than 0')
        
    else:
        for n in range(principal_quantum_number):
            l.append(n)
        return l
    
    


# Function for determining the rate constant of a reaction using the Arrhenius equation 

def arrhenius_equation(pre_exponential_factor, activation_energy, 
                       temperature):
    '''
    This function should return the rate constants, k for a reaction 
    with a given activation energy, Ea and pre-exponential factor, A, and 
    at a range of temperatures 
    
    Parameters:
        pre_exponential_factor (float): the pre exponential factor, A 
        activation_energy (float): the activation energy, Ea in Joules per mole
        temperature (float): the temperature of the system in kelvin
        
    Return:
        float: the rate constant at a range of temperatures
    '''
    k = pre_exponential_factor * np.exp(
        (-activation_energy)/(R*temperature)
    )
    
    return k


# Function for the Morse potential of a chemical bond at a given set of distances

def morse(dissociation_energy, r, r_e):
    """
    calculates the energy of a morse potential at a given set of distances
    
    Parameters:
        dissociation_energy (float): the bond dissociation energy in J per mol
        r (float): bond length
        r_e (float): equilibrium bond length
    
    Return:
        float: the energy of the morse potential
    """  
    
    E = dissociation_energy * (1 - np.exp (- (r - r_e ) ) ) **2
    
    
    return E


# Function that works out the pH of a solution given the concentration of the H+ ion

def pH(conc_h):
    '''
    Determines the pH for a given H+ concentration
    
    Parameters:
        conc_h (float): Concentration of H+ (or H3O+) in solution
        
    Returns:
        float: The pH value
    '''
    return np.log10(conc_h)


# Function that calculates how many electrons can reside in an orbital, given the principle quantum number (PQN) of the orbital

def elec_accom(n):
    """
    Calculates how many electrons in an orbital based on PQN
    
    Parameters:
        n (int): PQN
        
    Returns:
        int: electron occupancy
    """
    if not isinstance(n, int):
        raise TypeError('the PQN (n) '
                        'must be an integer')
    if n <= 0:
        raise ValueError('The PQN '
                         'must be greater than 0')
    else:
        return 4*n-2

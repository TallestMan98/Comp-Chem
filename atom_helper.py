import numpy as np

def distance(a,b):
    """
    Determines the dintance between two points in any number of dimensions
    """
    return np.sqrt(np.sum(np.square(a-b)))

def energy_lj(r, A, B):
    """
    determines Lennard-Jones potential between two atoms at any distance
    """
    return ((A/(r**12))-(B/(r**6)))
    
def energy_prime(r, A, B):
    """
    determines the first derivative of energy_lj
    """
    return ((6*B/(r**7))-(12*A/(r**13)))

def energy_prime_prime(r, A, B):
    """
    determines the second derivative of energy_lj
    """
    return ((156*A/(r**14))-(42*B/(r**8)))


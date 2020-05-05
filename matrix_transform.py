import numpy as np

def matrix_rotation(x, y, beta):
    '''
    does a matrix roation on a set of x y coordinates
    '''
    matrix = np.array([[np.cos(beta), -np.sin(beta)],
                      [np.sin(beta), np.cos(beta)]]) 
    
    old_coords = np.array([x, y])
    new_coords = np.matmul(matrix, old_coords)
    return new_coords
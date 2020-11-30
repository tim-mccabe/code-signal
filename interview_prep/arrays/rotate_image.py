import numpy as np

def rotateImage(a):
    b = np.rot90(a)
    c = np.rot90(b)
    return np.rot90(c).tolist()
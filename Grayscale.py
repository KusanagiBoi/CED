import numpy as np

def tgs (img: np.ndarray):
    b, g, r = img[..., 0], img[..., 1], img[..., 2]
    grayscale = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return grayscale
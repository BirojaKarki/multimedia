import numpy as np

def dct(signal):
    """Compute the 1D Discrete Cosine Transform of the input signal."""
    
    # Calculate the length of the input signal
    N = len(signal)
    
    # Initialize the DCT coefficients array
    dct_coef = np.zeros(N)
    
    # Compute the DCT coefficients
    for k in range(N):
        total = 0  # Changed from 'sum' to 'total' to avoid conflict with built-in function
        for n in range(N):
            total += signal[n] * np.cos(np.pi * k * (2*n + 1) / (2*N))
        dct_coef[k] = total * np.sqrt(2 / N)
    
    # Apply the scaling factor to the first coefficient
    if k == 0:
        dct_coef[k] *= np.sqrt(1 / 2)
    
    return dct_coef

signal = [1, 2, 3, 4, 5]
dct_coef = dct(signal)
print(dct_coef)
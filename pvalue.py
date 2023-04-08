import scipy.stats as st
import numpy as np
import math

def ensure_array(arrayable):
    """
    Ensures that data is an np array
    """
    if isinstance(arrayable, np.ndarray):
        return arrayable
    else:
        return np.array(arrayable)

def p_value_calculation(data, effect_size, alpha):

    data = ensure_array(data)

    x = effect_size * math.sqrt(len(data)) + st.norm.ppf(1 - alpha)

    return 1 - st.norm.cdf(x)


data = np.random.rand(50).tolist()

print(p_value_calculation(data, 0.10, 0.05))
import pandas as pd
import numpy as np

# Series - single dimension, size immutable

## From numpy array
a1 = np.array(['a', 'b', 'c', 'd'])
s1 = pd.Series(a1)
print(s1)

## From dictionary
d1 = {'k1': 0, 'k2': 100, 'k3': 200}
s2 = pd.Series(d1)
print(s2)

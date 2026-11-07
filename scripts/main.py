import numpy as np
from sklearn.linear_model import LinearRegression

data = np.genfromtxt("data/UNSW_NB15_testing-set(in).csv", delimiter=",")

print(data[:10])

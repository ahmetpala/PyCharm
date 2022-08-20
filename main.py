import numpy as np
import matplotlib.pyplot as plt

#%%
def name_as_uppercase(name):
    return name.upper()

name_as_uppercase('amina koyayim')

aa = np.array([1, 2, 3, 4, 5])
bb = aa**2

plt.scatter(aa, bb)
plt.show()

#%%
def check_balance(amount_paid, loan):
    return amount_paid - loan



#%%

import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return (x**0.5 - x*0.2)**0.1

xline = np.linspace(-30,30,num=200)
yline=f(xline)

plt.figure(num=0,dpi=128)
plt.plot(xline, yline)

plt.title("Quadratische Funktionen")
plt.xlabel("x / cm")
plt.ylabel("f(x) / cm")
# %%

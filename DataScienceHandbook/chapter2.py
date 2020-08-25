import numpy as np
import matplotlib as mpl
import  matplotlib.pyplot as plt

plt.style.use('classic')

x = np.linspace(0,10,100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')


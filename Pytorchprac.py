import matplotlib.pyplot as plt
import numpy as np
import torch
#FIXME: 。。。。
#TODO:。。。。
x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot
torch.cuda.is_available() # torch的cuda是否可用
from torch.utils.data import Dataset
# Dataset??
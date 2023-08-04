#today we will learn about matplotlib 
# so what is matplotlib ?
# it is mostly written in python a few segments are written in C,objectives-c and js for platform compatibility.
# it is a low level graph plotting library in python that serves as visualizition utility.
#it  is mostly used is data science.

# import matplotlib

# print(matplotlib.__version__)

#pyplot=> most of the matplotlib lies under the pyplot and are ususally imported under the plt alis:


#draw a line in a diagram from (0,0) to position (6,250):

import matplotlib.pyplot as plt
import numpy as np


xpoints=np.array([0,6])

ypoints=np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()





from scipy.stats import binom # Importe da distribuição binomial 
from scipy.stats import poisson #import da disttribuição poisson
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#from math import factorial
import math
#Importação das libs
valorB = binom.rvs(10**2,0.3,size = 80)
valorP = poisson.rvs(30, size = 80)
#
sns.distplot(valorB, hist = False)
sns.distplot(valorP, hist = False)
plt.xlim([0,80])
plt.xlabel('k')
plt.ylabel('P(X=k)')
plt.legend()
plt.show()
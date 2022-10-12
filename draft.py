import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
import math

warnings.filterwarnings("ignore")
import scipy as sp
from scipy import stats
from scipy.optimize import curve_fit

# ----DATA----
x = np.arange(1, 41)
zelan = [-12, 8, -17, -4, -2, -4, -8, -14, 2, 0, -89, -91, -46.5, -17.5, -72.5, -15, -39.5, -8.5, -29, -10, -30, -16,
         -27, -2, -11.5, -14.5, -32.5, -21.5, -14, 4, 35.7, 9, 1.9, 23, 1.4, -4.3, -21.3, 8.5, 7, 18.5]
hirata = [11, -24, 4, 6, -10, 5, 6, 0, -13, -1, -58, -60, -68, -57, -45, -27, -53, -15, -24, -3, -33, -15, -4, -27, -16,
          -21, -5, -22, 3, -12, 50, 26, 25, 34, 33, 18, 17, 36, 4, 13]
alex = [15, 13, 12, 1, 7, 9, 15, 12, 3, 6, -6, 10, 10.6, 15.2, 10, 6.6, 18, 8, 19.1, 24.3, 21.9, 19.0, 6.33, 19.04, 2.9,
        12.6, 1.8, 12.7, 7.06, 7.6, 20.1, 4.0, 2.3, 3.7, 6.28, 12.8, 10.4, 7.5, 7.6, 7.06]
lison = [29, 32, -12, -12, 20, -20, -23, 19, 40, 8, 40, 39, 40, 35, 22, 53, 6, -19, 26, 22, 1, 38, 0, 7, -12, 10, -2,
         -5, -9, 25, 4, 21, 2, 34, 8, 34, 25, 8, -16, 22]
luka = [2, -4, -23, 17, -24, 13, -16, -14, -14, -16, -88, -88, -53, -41, -81, -55, -12, -23, -30, -37, -16, -47, -54,
        -34, -29, -28, -30, -28, -29, -25, -26, -5, 14, 12, -2, 14, 17, 6, 3, -12]
ruben = [11, 5, 0.5, 9, -24.5, 5, -8.5, -9.5, -20, -0.5, -79, -66, -45.3, -46.5, -39, -35, -35, -26, -39, -36, -43.5,
         -35.5, -28.5, -21.5, -22, -16.5, -12.6, -27, -9.5, -21.6, 44, 41, 43.4, 34.5, 30.5, 12, 18, 13.6, 14.5, 17.5]


# -----AVERAGE-----
all_mean = []
for i in range(0, 40):
    all_mean.append((alex[i] + luka[i] + lison[i] + zelan[i] + hirata[i] + ruben[i]) / 6)


mu = np.mean(all_mean)
std = np.std(all_mean)
print("Mean: ",mu)
print("SD: ",std)

#---- PLOT
plt.scatter(x, all_mean, c='cyan')
plt.yticks(np.arange(-90, len(x) + 1, 15))
plt.axvline(x=10, linestyle='--')
plt.axvline(x=30, linestyle='--')
plt.title('Average')
plt.yticks(np.arange(-100, 75, 15))
plt.show()


#GAUSSIAN FUNCTION
def Gauss(x,mu,sigma):
    return 1/(sigma*np.sqrt(2*math.pi))*np.exp(-np.power())

#TASKS
#Get every 6 points

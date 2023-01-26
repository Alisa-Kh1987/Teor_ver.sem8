from sklearn.linear_model import LinearRegression
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# 2= np.array([30,30,40, 40])
# y1= np.array([37, 47, 50, 60])

# n = 4

# b0 = np.mean(y1) - np.mean(2)
# print("b0 = ", b0)
# b1 = (n*np.sum(2*y1) - np.sum(2)*np.sum(y1))/(n*np.sum(2**2) - np.sum(2)**2)
# print("b1 = ", b1)

# yp = b0 + 2*b1

# r = np.corrcoef(2, y1)
# print("corrcoef = ", r)

# plt.scatter(2, y1)
# plt.plot(2, b0+b1+2)
# plt.title('r= вписать значение коэффициента')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# x2= np.array([30,30,40, 40, 20, 20, 50, 50]) 
# y2= np.array([37, 47, 50, 60, 25, 35, 62, 72]) 


# n = 8

# b1 = (n*np.sum(x2*y2) - np.sum(x2)*np.sum(y2))/(n*np.sum(x2**2) - np.sum(x2)**2)
# print("b1 = ", b1)

# b0 = np.mean(y2) - b1*np.mean(x2)
# print("b0 = ", b0)

# yp = b0 + x2*b1

# r = np.corrcoef(x2, y2)
# print("corrcoef = ", r)

# plt.scatter(x2, y2)
# plt.plot(x2, (b0 + b1*x2))
# plt.title('r= вписать значение коэффициента')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
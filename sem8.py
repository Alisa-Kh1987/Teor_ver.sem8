import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

cov = np.mean(zp*ks) - np.mean(zp)*np.mean(ks)
r_my = cov / (np.std(zp) * np.std(ks))
print("cov: ", cov)
print("r_my: ", r_my)

# plt.scatter(zp, ks)
# plt.title('r= вписать значение коэффициента')
# plt.xlabel('zp')
# plt.ylabel('ks')
# plt.show()
# plt.plot(zp, ks)
print ("cov2: ", np.cov(zp, ks, ddof=0))
print("corrcov:", np.corrcoef(zp, ks))
# import numpy as np
# import scipy.stats as stats

# x1 = np.array([380, 420, 290])
# y1 = np.array([140, 360, 200, 900])

# result = stats.mannwhitneyu(x1, y1)
# # MannwhitneyuResult(statistic = 8, pvalue = 1.0)
# print(result)

# import numpy as np
# import scipy.stats as stats

# press_before = np.array([150, 160, 165, 145, 155])
# min10_press = np.array([140, 155, 150, 130, 135])
# min30_press = np.array([130, 130, 120, 130, 125])

# print(stats.friedmanchisquare(press_before, min10_press, min30_press))

# import numpy as np
# import scipy.stats as stats

# press_before = np.array([150, 160, 165, 145, 155])
# min10_press = np.array([140, 155, 150, 130, 135])

# print (stats.wilcoxon(press_before, min10_press))

# import numpy as np
# import scipy.stats as stats

# group1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
# group2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
# group3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

# print(stats.kruskal(group1, group2, group3))

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

x4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89])


plt.scatter(x4, y4)
plt.title('r= вписать значение коэффициента')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(np.corrcoef(x4,y4))
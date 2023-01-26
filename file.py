# import numpy as np
# from scipy import stats

# # x = np.array([10.50, 9.94, 10.42, 10.47, 10.4, 9.93, 9.17, 9.26, 10.11, 10.15, 10.5, 10.47])
# # np.mean(x)
# # print(np.mean(x))

# x =np.array([2.5, 2.2, 2.6, 2, 2.1, 1.8,2.4, 2.3, 2.7, 2.7, 1.9])
# y= np.array([2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2])

# np.mean(x)
# print(np.mean(x))

# np.mean(y)
# print(np.mean(y))

# print()

# np.var(x)
# print(np.var(x))

# np.var(y)
# print(np.var(y))

# print()

# result = stats.ttest_ind(x, y)
# print(result)

# new_res = (np.mean(x) - np.mean(y) )/np.sqrt((np.var(x)/len(x)) + (np.var(y)/len(y)))
# print(new_res)


# import numpy as np
# import scipy.stats as stats
 
# height_moth = np.array([172, 177, 158, 170, 178,175, 164, 160, 169])
# height_daug = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])
 
# var_mother = np.var(height_moth, ddof=1)
# print(var_mother)
# print()
# var_daughter = np.var(height_daug, ddof=1)
# print(var_daughter)
 
# mean_mother = np.mean(height_moth)
# mean_daughter = np.mean(height_daug)
 
# l_mother = len(height_moth)
# print()
# print(l_mother)
# l_daughter = len(height_daug)
# print()
# print(l_daughter)
# t1 = stats.t.ppf(0.975, 8)
# t2 = stats.t.ppf(0.975, 8) 
# print(f"t теор. для матерей {t1:.3f}, t теор. для дочерей {t2:.3f}")
# t = (var_mother - var_daughter) / np.sqrt((var_mother/l_mother) + (var_daughter/l_daughter))
# print(f"t рассчит.{t:.3f}")


# from scipy import stats

# print ('В представленной задаче у нас двухвыборочный тест,с зависимыми выборками, решим с помощью  применения функций:') 
# # Нулевая гипотеза различий нет - μ=μ0
# # Альтернативная гипотеза, есть статистически значимые различия - μ≠ μ0
# moth_height = ([172, 177, 158, 170, 178,175, 164, 160, 169])
# daug_height =([173, 175, 162, 174, 175, 168, 155, 170, 160])
# alfa=0.05
# print (stats.ttest_rel(a = moth_height, b = daug_height))
# Статистика t-теста равна 0.5595, двустороннее значение p равно 0.5911.
# print ('Так как p > a, то мы принимаем нулевую гипотезу, то есть статистически значимых различий нет.')
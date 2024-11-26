import numpy as np
from scipy.linalg import inv, det
from scipy.spatial.distance import mahalanobis

# Данные задачи
mu1 = np.array([5, 1])
mu2 = np.array([-4, -6])

# Матрицы ковариации
Sigma1 = np.array([[6, 1], [1, 30]])
Sigma2 = np.array([[1, 2], [2, 11]])

# Вычисление обратных матриц ковариации
inv_Sigma1 = inv(Sigma1)
inv_Sigma2 = inv(Sigma2)

# Вычисление разности между двумя квадратичными формами
A = inv_Sigma1 - inv_Sigma2
B = 2 * (np.dot(mu2, inv_Sigma2) - np.dot(mu1, inv_Sigma1))
C = (np.dot(mu1, np.dot(inv_Sigma1, mu1)) - np.dot(mu2, np.dot(inv_Sigma2, mu2))
     - np.log(det(Sigma2) / det(Sigma1)))

# Формирование квадратичной формы: x^T A x + B x + C = 0
# Для нахождения осей эллипса нам интересна матрица A
eigvals, eigvecs = np.linalg.eig(A)

# Длина большей полуоси эллипса
major_axis_length = 2 / np.sqrt(np.min(np.abs(eigvals)))  # Берем минимальное собственное значение для большей полуоси

print(major_axis_length)
# 8.82
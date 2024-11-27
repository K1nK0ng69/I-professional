import numpy as np

# Ввод размеров изображения
m, n = map(int, input("Введите размеры изображения (m,n): ").replace(',', ' ').split())
# Ввод изображения
image = [list(map(int, input("Введите строки изображения: ").replace(',', ' ').split())) for _ in range(m)]

# Ввод размеров результата
m_result, n_result = map(int, input("Введите размеры результата свёртки (m_result,n_result): ").replace(',', ' ').split())
# Ввод результата свёртки
result = [list(map(int, input("Введите строки результата: ").replace(',', ' ').split())) for _ in range(m_result)]

# Определяем размеры ядра
kernel_height = m_result - m + 1
kernel_width = n_result - n + 1

# Проверка на допустимость размеров ядра
if kernel_height <= 0 or kernel_width <= 0:
    raise ValueError("Размеры результата свёртки должны быть больше размеров изображения.")

# Создаем матрицу A и вектор b
A = []
b = []

# Заполняем матрицу A и вектор b
for i in range(m_result):
    for j in range(n_result):
        # Для каждого элемента результата создаем соответствующее уравнение
        if i < kernel_height and j < kernel_width:
            row = []
            # Составляем уравнение для текущего элемента результата
            for ki in range(m):
                for kj in range(n):
                    row.append(image[ki][kj])
            A.append(row)
            b.append(result[i][j])

# Преобразуем в массив NumPy
A = np.array(A)
b = np.array(b)

# Проверка на достаточное количество уравнений
if len(b) == 0 or len(A) == 0 or A.shape[0] < kernel_height * kernel_width:
    raise ValueError("Недостаточно уравнений для определения ядра.")

# Решаем систему уравнений
kernel_values, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

# Проверка на правильное количество элементов для reshaping
if kernel_values.size != kernel_height * kernel_width:
    raise ValueError(f"Невозможно сформировать ядро из {kernel_values.size} элементов в форму ({kernel_height}, {kernel_width}).")

# Формируем ядро свёртки из полученных значений
kernel = kernel_values.reshape(kernel_height, kernel_width)

# Выводим результат
for row in kernel:
    print(','.join(map(str, map(int, row))))

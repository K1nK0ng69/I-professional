import math
import numpy as np
from scipy.stats import pearsonr
import time
import threading

def solve():
    # Инициализация значений
    lambda_val = float(1.00000)  # Значение λ
    x0, x1, x2 = float(1.85006), float(2.66777), float(7.77955)  # Пороги x0, x1, x2

    # Начальные значения для квантования: y0 = 0, y1, y2, y3
    y_values = [0, 0, 0, 0]  # Инициализация

    # Определяем оптимальные значения для квантования
    y1 = 0.31681  # Примерный коэффициент
    y2 = 0.42933  # Примерный коэффициент
    y3 = 0.84576  # Примерный коэффициент

    # Нормировка значений y0, y1, y2, y3
    norm_factor = 1.0 / math.sqrt(y1 ** 2 + y2 ** 2 + y3 ** 2)
    y1 *= norm_factor
    y2 *= norm_factor
    y3 *= norm_factor

    # Формируем финальные значения
    y_values[1] = y1
    y_values[2] = y2
    y_values[3] = y3

    # Генерация данных и применение квантования
    x = np.random.laplace(0, lambda_val, 10000)  # Пример сгенерированных данных из распределения Лапласа
    y = np.zeros_like(x)

    # Применяем симметричное квантование
    for i in range(len(x)):
        if abs(x[i]) <= x0:
            y[i] = 0
        elif x0 < abs(x[i]) <= x1:
            y[i] = y1 if x[i] > 0 else -y1
        elif x1 < abs(x[i]) <= x2:
            y[i] = y2 if x[i] > 0 else -y2
        else:
            y[i] = y3 if x[i] > 0 else -y3

    # Корреляция Пирсона между x и y
    correlation = pearsonr(x, y)[0]

    # Выводим результат
    print(f"{correlation:.5f}")
    print(f"{y_values[0]:.5f},{y_values[1]:.5f},{y_values[2]:.5f},{y_values[3]:.5f}")

def run_with_timeout(timeout):
    thread = threading.Thread(target=solve)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print("Время выполнения превысило лимит в 1 секунду.")
        thread.join()  # Дождаться завершения потока (если он завершится позже)

# Начало измерения времени
start_time = time.time()

# Запуск функции с ограничением по времени
run_with_timeout(1)

# Конец измерения времени
end_time = time.time()

# Вывод времени выполнения
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.5f} секунд")

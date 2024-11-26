def calculate_average_precision(data):
    # Определение порогов
    thresholds = [i * 0.1 for i in range(10)]

    # Список для хранения точностей для каждого порога
    precisions = []

    # Цикл по каждому порогу
    for threshold in thresholds:
        tp = 0  # True Positives
        fp = 0  # False Positives

        # Прогнозирование по каждому значению с учетом порога
        for prob, actual in data:
            predicted = 'Спелый' if prob >= threshold else 'Неспелый'

            if predicted == 'Спелый':
                if actual == 'Спелый':
                    tp += 1
                else:
                    fp += 1

        # Вычисление точности
        if tp + fp == 0:
            precision = 1.0  # Если нет предсказанных положительных, точность считается 1
        else:
            precision = tp / (tp + fp)

        precisions.append(precision)

    # Вычисление Average Precision
    average_precision = sum(precisions) / len(precisions)

    # Возврат результата, округленного до двух знаков после запятой
    return round(average_precision, 2)


# Данные: (вероятность предсказания, истинная метка)
data = [
    (0.85, 'Спелый'),
    (0.55, 'Спелый'),
    (0.65, 'Неспелый'),
    (0.40, 'Спелый'),
    (0.95, 'Спелый'),
    (0.75, 'Неспелый'),
    (0.50, 'Спелый'),
    (0.60, 'Спелый'),
    (0.30, 'Неспелый'),
    (0.80, 'Спелый')
]

# Расчет и вывод Average Precision
ap = calculate_average_precision(data)
print(f"Average Precision: {ap}")

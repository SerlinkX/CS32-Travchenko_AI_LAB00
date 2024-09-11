import numpy as np

# Функція для пошуку максимального елемента після нуля
def max_after_zero(x):
    # Знаходимо індекси елементів, які йдуть після нуля
    indices = np.where(x[:-1] == 0)[0] + 1
    # Якщо таких індексів немає, повертаємо None
    if len(indices) == 0:
        return None
    # Повертаємо максимальний елемент
    return np.max(x[indices])

# Функція для пошуку найближчого до числа елемента в матриці
def closest_value(X, v):
    # Знаходимо елемент, який найменше відрізняється від v
    return X.flat[np.abs(X - v).argmin()]

# Функція для масштабування стовпців матриці
def scale_columns(X):
    # Копіюємо матрицю, щоб не змінювати оригінал
    X_scaled = X.copy().astype(float)
    # Обробляємо кожен стовпець окремо
    for col in range(X.shape[1]):
        max_val = np.max(X[:, col])
        # Якщо максимальний елемент не нуль, виконуємо масштабування
        if max_val != 0:
            X_scaled[:, col] /= max_val
    return X_scaled

# Приклад використання функцій:

# Функція max_after_zero
x = np.array([6, 2, 0, 3, 0, 0, 9, 7, 0])
print("Максимальний елемент після нуля:", max_after_zero(x))

# Функція closest_value
X = np.arange(0, 10).reshape((2, 5))
v = 7.2
print("Найближчий елемент до числа", v, ":", closest_value(X, v))

# Функція scale_columns
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Масштабована матриця:\n", scale_columns(matrix))

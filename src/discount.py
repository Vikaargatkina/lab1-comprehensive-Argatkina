import os

def calculate_discount(price):
    # Эта строка специально сделана очень длинной, чтобы flake8 выдал ошибку E501 (line too long)
    return price - 100 if price > 5000 else price

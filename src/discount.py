def calculate_discount(price):
    # Разбиваем длинный комментарий на две строки
    # чтобы он не превышал лимит в 80 символов
    return price - 100 if price > 5000 else price

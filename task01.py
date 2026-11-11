result = [("Оплата", 0.25), ("Доставка", 0.91), ("Возврат", 0.62), ("Адрес", 0.13)]
result.sort(key=lambda item: item[1], reverse=True)

print(f"{result[0][0]} {result[0][1]:.3f}")
print(f"{result[1][0]} {result[1][1]:.3f}")

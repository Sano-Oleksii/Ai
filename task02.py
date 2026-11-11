from sklearn.metrics.pairwise import cosine_similarity
chunks = ["Оплата", "Доставка", "Возврат", "Адрес"]
query = [[1.0, 0.0]]
vectors = [[0.0, 1.0], 
           [1.0, 0.0], 
           [0.8, 0.6], 
           [-1.0, 0.0]]
matrix = cosine_similarity(query, vectors)
print(matrix.shape)
scores = matrix[0]
indices = scores.argsort()
# Получаем индексы от самой маленькой оценки к самой большой.
descending = indices[::-1]
# Разворачиваем последовательность индексов в убывающий порядок оценок.
top_indices = descending[:2]
# Берем первые два индекса — это top-2.
for index in top_indices:
# Перебираем выбранные позиции в порядке убывания сходства.
    print(chunks[index], f"{scores[index]:.3f}")
    # По одному индексу достаем связанный текст и его оценку.


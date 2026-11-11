from sentence_transformers import SentenceTransformer
# Подключаем загрузку модели embeddings.
from sklearn.metrics.pairwise import cosine_similarity
# Подключаем вычисление сходства для строк числовых таблиц.
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu",local_files_only=True)
# Создаем одну модель до кодирования всех слов примера.
texts = ["shipping", "delivery", "banana"]
# Берем два слова о доставке и одно слово о фрукте.
vectors = model.encode(texts, show_progress_bar=True)
# Получаем таблицу из трех векторов в порядке texts.
near = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
# Сравниваем shipping с delivery и достаем числовую оценку.
far = cosine_similarity([vectors[0]], [vectors[2]])[0][0]
# Сравниваем shipping с banana той же операцией.

print(f"shipping / delivery: {near:.3f}")
# Печатаем первую оценку с тремя знаками после точки.
print(f"shipping / banana: {far:.3f}")
# Печатаем вторую оценку в том же формате.

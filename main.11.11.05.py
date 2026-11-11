from sentence_transformers import SentenceTransformer
# Подключаем загрузку модели embeddings.
from sklearn.metrics.pairwise import cosine_similarity
# Подключаем сравнение запроса со всей базой.
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
# Используем английскую модель для примера из плана архива.
chunks = ["buy insurance policy", "weather is nice today"]
# Добавляем фрагменты о покупке полиса и о погоде.
chunks += ["insurance claim process", "how to cook pasta"]
# Добавляем тексты о страховом случае и приготовлении еды.
chunk_vectors = model.encode(chunks, show_progress_bar=False)
# Считаем векторы базы в том же порядке, что и тексты.
query_vector = model.encode(["insurance"], show_progress_bar=False)
# Получаем таблицу с одним вектором запроса о страховании.
scores = cosine_similarity(query_vector, chunk_vectors)[0]
# Достаем строку из четырех оценок.
indices = scores.argsort()[::-1][:2]
# Получаем позиции двух самых высоких оценок.
for index in indices:
# Перебираем два выбранных индекса.
    print(chunks[index], f"{scores[index]:.3f}")
    # Выводим текст каждого кандидата и его сходство с запросом.
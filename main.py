from sentence_transformers import SentenceTransformer
# Импортируем класс для создания объекта модели.
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu", local_files_only=True)
# Загружаем модель для английских учебных текстов на обычный процессор.
embedding = model.encode("Hello World!", show_progress_bar=False)
# Получаем один вектор из одной переданной строки.
print(embedding.shape)
# Выводим форму массива одного embedding.
texts = ["shipping", "delivery", "cat"]
# Подготавливаем три текста в определенном порядке.
embeddings = model.encode(texts, show_progress_bar=False)
# Получаем одну строку координат на каждый текст списка.
print(embeddings.shape)
# Проверяем число строк и число координат в каждой строке.
print(embeddings[0].shape)
# Берем первую строку, то есть вектор текста shipping.
# show_progress_bar - полоса, показывающая процесс выполнения чего-то
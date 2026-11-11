from sentence_transformers import SentenceTransformer
# Подключаем класс моделей для получения embeddings.
from sklearn.metrics.pairwise import cosine_similarity
# Подключаем функцию сравнения векторов.
name = "paraphrase-multilingual-MiniLM-L12-v2"
# Выбираем многоязычную модель из русского примера архива.
model = SentenceTransformer(name, device="cpu",local_files_only=True)
# Загружаем ее один раз перед кодированием трех фраз.
texts = []
# Создаем список фраз в заранее известном порядке.
texts.append("Я попал в ДТП и повредил свой автомобиль")
# Добавляем описание автомобильной аварии.
texts.append("Со мной случилась авария, помял крыло моей машины")
# Добавляем ту же тему, выраженную другими словами.
texts.append("Я отлично прогулялся вчера пешком и отдохнул")
# Добавляем фразу о прогулке для сравнения.
vectors = model.encode(texts, show_progress_bar=False)
# Превращаем все три фразы в строки числовой таблицы.
scores = cosine_similarity([vectors[0]], vectors)[0]
# Сравниваем первую фразу со всеми тремя и берем строку оценок.
for index, score in enumerate(scores):
# Перебираем позицию и оценку каждого сравниваемого текста.
    print(index, f"{score:.3f}")
    # Печатаем индекс фразы и ее сходство с первой фразой.
scores = cosine_similarity([vectors[0]], vectors)[0][0]
# цикл for не сработает с этим примером , так как тут [0][0]
# и enumerate(scores) не может перебрать один элемент
# а в первом примере все работает, так как там 3 элемента сравнения.
print(scores)
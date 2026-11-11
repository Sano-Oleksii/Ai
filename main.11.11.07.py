from pathlib import Path
# Подключаем построение путей относительно файла модуля.
def get_database_path():
# Выносим путь в функцию, чтобы использовать его при записи и чтении.
    current_dir = Path(__file__).resolve().parent
    # Получаем папку rag/ingestion.
    return current_dir.parent.parent / "database" / "database.txt"
    # Возвращаем путь к текстовой базе в корне проекта.
def save(vectors):
# Принимаем пары вектор и текст, созданные get_vectors.
    path = get_database_path()
    # Получаем полный путь к файлу базы.
    path.parent.mkdir(parents=True, exist_ok=True)
    # Создаем папку database, если ее еще нет.
    with open(path, "w", encoding="utf-8") as database:
    # Открываем базу на перезапись, чтобы повторный запуск не дублировал записи.
        for vector, text in vectors:
        # Из каждой пары отдельно получаем числовой массив и текст.
            vector_str = " ".join(map(str, vector))
            # Превращаем координаты в одну строку с пробелами между числами.
            database.write(f"{vector_str};{text}\n")
            # Записываем числа, разделитель, текст и завершающий перенос строки.

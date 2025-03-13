import requests
import os
from git import Repo


# Константы
CODERWARS_API_URL = "https://www.codewars.com/api/v1"
USERNAME = "karsakov-a"  # Замените на ваше имя пользователя
OUTPUT_DIR = "F:\\Dev\\_codewars"  # Папка для сохранения решений
GIT_REPO_PATH = OUTPUT_DIR  # Путь к локальному Git-репозиторию
GIT_REPO_URL = "https://github.com/karsakov-a/codewars-solutions.git"  # URL вашего репозитория
GIT_COMMIT_MESSAGE = "Add new Codewars solutions"

# Создаем папку для решений
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Проверка работы API
test_url = f"{CODERWARS_API_URL}/users/{USERNAME}"
response = requests.get(test_url)
if response.status_code == 200:
    print("API работает корректно")
else:
    print(f"Ошибка при тестировании API: {response.status_code}")
    exit()

# Функция для получения списка завершенных ката
def get_completed_katas(username):
    url = f"{CODERWARS_API_URL}/users/{username}/code-challenges/completed"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("data", [])
    elif response.status_code == 404:
        print("Ошибка 404: Проверьте имя пользователя или настройки приватности.")
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
    return []

# Основная функция
def main():
    print("Получение списка завершенных ката...")
    completed_katas = get_completed_katas(USERNAME)

    saved_slugs = set()  # Множество для отслеживания уже сохраненных задач

    for kata in completed_katas:
        print(f"Обработка ката: {kata['slug']}")

        # Проверяем, что файл еще не был сохранен
        if kata["slug"] in saved_slugs:
            continue

        # Извлекаем информацию о ката
        language = kata["completedLanguages"][0] if kata["completedLanguages"] else "unknown"
        slug = kata["slug"]

        # Если язык не Python, пропускаем задачу
        if language.lower() != "python":
            continue

        # Создаем путь к файлу
        file_path = os.path.join(OUTPUT_DIR, f"{slug}.py")

        # Сохраняем метаданные вместо кода
        metadata = {
            "slug": kata["slug"],
            "name": kata["name"],
            "language": language,
            "completed_at": kata["completedAt"],
        }

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(metadata))  # Сохраняем метаданные как строку
        print(f"Сохранено: {file_path}")

        saved_slugs.add(slug)  # Добавляем slug в множество сохраненных

    print("Все метаданные успешно сохранены!")

    # Выполняем коммит и push в GitHub
    commit_to_github()


# Функция для отправки изменений в GitHub
def commit_to_github():
    try:
        print("Инициализация Git-репозитория...")
        repo = Repo(GIT_REPO_PATH)

        if not repo.bare:
            print("Репозиторий уже существует. Добавление изменений...")
        else:
            print("Инициализация нового репозитория...")
            repo = Repo.init(GIT_REPO_PATH)

        # Добавляем все новые файлы
        repo.git.add(all=True)

        # Создаем коммит
        repo.index.commit(GIT_COMMIT_MESSAGE)

        # Проверяем, есть ли удаленный репозиторий
        if "origin" not in [remote.name for remote in repo.remotes]:
            print("Настройка удаленного репозитория...")
            repo.create_remote("origin", GIT_REPO_URL)

        # Синхронизация с удаленным репозиторием
        print("Синхронизация с удаленным репозиторием...")
        remote = repo.remote(name="origin")
        remote.pull()  # Добавляем pull для синхронизации
        remote.push(refspec=f"HEAD:main", set_upstream=True)  # Явно указываем ветку main

        print("Успешно отправлено в GitHub!")
    except Exception as e:
        print(f"Ошибка при работе с Git: {e}")


if __name__ == "__main__":
    main()



def alphabet_position(text):
        # Словарь для отображения букв в их позиции
    alphabet = {chr(i + 96): i for i in range(1, 27)}
    
    # Заменяем буквы на их позиции и игнорируем всё остальное
    result = [
        str(alphabet[char.lower()]) 
        for char in text 
        if char.lower() in alphabet
    ]
    
    # Возвращаем строку с числами через пробел
    return " ".join(result)
import requests
import os

CODERWARS_API_URL = "https://www.codewars.com/api/v1"
USERNAME = "karsakov-a"
OUTPUT_DIR = "F:\\Dev\\_codewars"

def get_completed_katas(username):
    url = f"{CODERWARS_API_URL}/users/{username}/code-challenges/completed"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("Ошибка 404: Проверьте имя пользователя или настройки приватности.")
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
    return []

# Пример использования
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print("Получение списка завершенных ката...")
completed_katas = get_completed_katas(USERNAME)
print(completed_katas)
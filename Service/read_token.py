import json
import requests

with open("token.json", "r") as file:
    token_data = json.load(file)

access_token = token_data["access_token"]
print(f"Ваш токен: {access_token}")

headers = {
    "Authorization": f"OAuth {access_token}"
}

url = "https://cloud-api.yandex.net/v1/disk/"

response = requests.get(url, headers=headers)

print("HTTP статус:", response.status_code)
print("Ответ API:", response.text)

if response.status_code == 200:
    print("Токен валиден.")
    data = response.json()
    print("Данные API:", json.dumps(data, indent=4))
else:
    print("Ошибка при обращении к API.")

from django.shortcuts import render
import json
import urllib.request

def index(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '48a90ac42caa09f90dcaeee4096b9e53'
        # Сделать запрос к API и получить данные
        try:
            source = urllib.request.urlopen(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru').read()

            # Конвертировать json данные в словарь
            list_of_data = json.loads(source)

            # Извлечение нужных данных
            data = {
                "city": list_of_data['name'],  # Название города
                "country_code": list_of_data['sys']['country'],  # Код страны
                "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",  # Координаты
                "temp": list_of_data['main']['temp'],  # Температура
                "pressure": list_of_data['main']['pressure'],  # Давление
                "humidity": list_of_data['main']['humidity'],  # Влажность
            }
        except Exception as e:
            print(f"Ошибка: {e}")
            data = {"city": city, "error": "Не удалось получить данные о погоде."}

    return render(request, "main/index.html", data)

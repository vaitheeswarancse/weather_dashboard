import requests
from django.shortcuts import render
from .models import SearchHistory
from django.conf import settings

# Use the key from settings.py
WEATHERAPI_KEY = getattr(settings, 'WEATHERAPI_KEY', None)

def index(request):
    weather_data = None
    chart_data = []
    error = None

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if city:
            if not WEATHERAPI_KEY:
                error = "WeatherAPI key is missing. Please set it in settings.py."
            else:
                url = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={city}&aqi=no"
                try:
                    resp = requests.get(url, timeout=10)
                    data = resp.json()

                    # DEBUG: show API response
                    print("API response:", data)
                    print("Using WeatherAPI Key:", WEATHERAPI_KEY)

                    if resp.status_code == 200 and 'location' in data:
                        temperature = data['current']['temp_c']
                        humidity = data['current']['humidity']
                        condition = data['current']['condition']['text']

                        # Save search history
                        SearchHistory.objects.create(
                            city=city,
                            temperature=temperature,
                            humidity=humidity,
                            condition=condition
                        )

                        # Keep only last 5 searches
                        history = list(SearchHistory.objects.all().order_by('-created_at')[:5])
                        ids_to_keep = [h.id for h in history]
                        SearchHistory.objects.exclude(id__in=ids_to_keep).delete()

                        weather_data = {
                            'city': city,
                            'temperature': temperature,
                            'humidity': humidity,
                            'condition': condition,
                        }
                    else:
                        error = data.get('error', {}).get('message', 'Could not fetch weather data.')
                except requests.RequestException as e:
                    error = f'Network error while contacting WeatherAPI: {e}'

    # Chart data from last 5 searches
    history = SearchHistory.objects.all().order_by('-created_at')[:5]
    chart_data = [{'city': h.city, 'temp': h.temperature} for h in reversed(history)]

    return render(request, 'index.html', {
        'weather_data': weather_data,
        'chart_data': chart_data,
        'error': error,
    })

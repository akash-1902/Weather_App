import requests
from django.shortcuts import render
from .forms import CityForm

API_KEY = '7fcfed1837f7a4a88f75d9ce3c6d359b'

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def index(request):
    weather_data = None
    error = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)
            if weather_data.get('cod') != 200:
                error = weather_data.get('message', 'Error fetching data')
                weather_data = None
    else:
        form = CityForm()

    context = {
        'form': form,
        'weather_data': weather_data,
        'error': error
    }

    return render(request, 'index.html', context)


from django.shortcuts import render
from django.conf import settings
import requests
# Create your views here.
def HomeView(request):
    city = ''
    context = {}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    if request.method == 'POST':
        city = request.POST.get('city')
        try:
            r = requests.get(url.format(city, settings.WEATHER_KEY)).json()
            context = {
                'city' : city,
                'temp' : r['main']['temp'],
                'desc' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                'Not_Found' : None
            }
        except:
            context = {
                'city' : city,
                'temp' : '',
                'desc' : '',
                'icon' : '',
                'Not_Found' : 'Not Found'
            }
    return render(request, 'home.html', context)
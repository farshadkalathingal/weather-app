from django.shortcuts import render
from django.conf import settings
import requests
import datetime
# Create your views here.
def HomeView(request):
    city = ''
    context = {}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    if request.method == 'POST':
        city = request.POST.get('city')
        time = datetime.datetime.utcnow()
        try:
            r = requests.get(url.format(city, settings.WEATHER_KEY)).json()
            Celsius = round((int(r['main']['temp'])-32)*5/9, 1)
            feel = round(int(r['main']['feels_like']-32)*5/9)
           # print(r)
            context = {
                'city' : city,
                'temp' : Celsius,
                'feel' : feel,
                'pressure' : r['main']['pressure'],
                'humidity' : r['main']['humidity'],
                'desc' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                'time' : time + datetime.timedelta(0, r['timezone']),
                'Not_Found' : None
            }
        except:
            context = {
                'city' : city,
                'Not_Found' : 'Not Found'
            }
    return render(request, 'home.html', context)
from django.shortcuts import render
from django.conf import settings
import requests
import datetime
# Create your views here.
def HomeView(request):
    city = ''
    context = {}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    if request.method == 'POST':
        city = request.POST.get('city')
        time = datetime.datetime.utcnow()
        try:
            r = requests.get(url.format(city, settings.WEATHER_KEY)).json()
            arr = ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
            val=int((r['wind']['deg']/22.5)+.5)
            
            context = {
                'city' : r['name'],
                'country' : r['sys']['country'],
                'temp' : r['main']['temp'],
                'feel' : round(r['main']['feels_like']),
                'pressure' : r['main']['pressure'],
                'humidity' : r['main']['humidity'],
                'desc' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                'time' : time + datetime.timedelta(0, r['timezone']),
                'speed' : r['wind']['speed'],
                'dir' : arr[(val % 16)],
                'visible' : round(int(r['visibility']/1000), 1),
                'Not_Found' : None
            }
        except:
            context = {
                'city' : city,
                'Not_Found' : 'Not Found'
            }
    return render(request, 'home.html', context)
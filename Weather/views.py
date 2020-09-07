from django.shortcuts import render
from django.conf import settings
import requests
import datetime
import pytz
# Create your views here.
def HomeView(request):
    city = ''
    context = {}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    api = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&units=metric&appid={}'
    if request.method == 'POST':
        city = request.POST.get('city')
        time = datetime.datetime.utcnow()
        try:
            r = requests.get(url.format(city, settings.WEATHER_KEY)).json()
            arr = ["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
            
            all = requests.get(api.format(r['coord']['lat'], r['coord']['lon'], settings.WEATHER_KEY)).json()
            val=int((all['current']['wind_deg']/22.5)+.5)
            #print(all)
            current_weather = {
                'temp' : round(all['current']['temp']),
                'feel' : round(all['current']['feels_like']),
                'pressure' : all['current']['pressure'],
                'humidity' : all['current']['humidity'],
                'desc' : all['current']['weather'][0]['description'],
                'icon' : all['current']['weather'][0]['icon'],
                'time' : time + datetime.timedelta(0, all['timezone_offset']),
                'speed' : all['current']['wind_speed'],
                'dir' : arr[(val % 16)],
                'visible' : round(int(all['current']['visibility']/1000), 1),
                'uv' : round(all['current']['uvi']),
                'dew_p' : round(all['current']['dew_point']),
            }
            daily_weather = []
            for d in all['daily']:
                #print(datetime.datetime.utcfromtimestamp(d['dt']).replace(tzinfo=pytz.utc))
                val=int((d['wind_deg']/22.5)+.5)
                daily = {
                    'dt' : datetime.datetime.utcfromtimestamp(d['dt']).replace(tzinfo=pytz.utc),
                    'sunrise' : datetime.datetime.utcfromtimestamp(d['sunrise']).replace(tzinfo=pytz.utc),
                    'sunset' :  datetime.datetime.utcfromtimestamp(d['sunset']).replace(tzinfo=pytz.utc),
                    'max' : round(d['temp']['max']),
                    'min' : round(d['temp']['min']),
                    'morn' : round(d['temp']['morn']),
                    'day' : round(d['temp']['day']),
                    'eve' : round(d['temp']['eve']),
                    'night' : round(d['temp']['night']),
                    'f_morn' : round(d['feels_like']['morn']),
                    'f_day' : round(d['feels_like']['day']),
                    'f_eve' : round(d['feels_like']['eve']),
                    'f_night' : round(d['feels_like']['night']),
                    'pressure' : d['pressure'],
                    'humidity' : d['humidity'],
                    'dew' : d['dew_point'],
                    'w_speed' : d['wind_speed'],
                    'w_dire' : arr[(val % 16)],
                    'desc' : d['weather'][0]['description'],
                    'icon' : d['weather'][0]['icon']        
                }
                daily_weather.append(daily)
            
            #print(daily_weather)

            context = {
                'city' : r['name'],
                'country' : r['sys']['country'],
                'current' : current_weather,
                'daily' : daily_weather,
                'Not_Found' : None
            }
        except:
            context = {
                'city' : city,
                'Not_Found' : 'Not Found'
            }
    return render(request, 'home.html', context)
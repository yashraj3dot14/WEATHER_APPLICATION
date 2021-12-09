from django.shortcuts import render,redirect
import requests
API_KEY = '#'
# Create your views here.
def home(request):
    city = request.GET.get('city')
    if city:
        try:
            url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes'
            resonse = requests.get(url)
            data = resonse.json()
            location = data['location']
            temperature = data['current']
        except:
            return render(request,'weatherApp/error.html')
    else:
        url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Delhi&aqi=yes'
        resonse = requests.get(url)
        data = resonse.json()
        location = data['location']
        temperature = data['current']
    context = {'location': location, 'temperature': temperature}
    return render(request,'weatherApp/home.html', context)

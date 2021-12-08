from django.shortcuts import render,redirect
import requests
API_KEY = '5b87951dd8414ad094c154044210612'
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

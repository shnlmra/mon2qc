from django.shortcuts import render
from django.http import JsonResponse
import requests



def home_view(request):
    return render(request, 'home/home.html')  # adjust this path to where your template really is

def routes_view(request):
    # Example placeholder response
    return render(request, 'routes/routes.html')

def terminal_view(request):
    # Example placeholder response
    return render(request, 'terminal/terminal.html')

def traffic_view(request):
    # Example placeholder response
    return render(request, 'traffic/traffic.html')

def predict_delay(request):
    route = request.GET.get('route', 'default')
    hour = request.GET.get('hour')

def ibp (request):
    return render (request, 'routes/ibp.html')

def cmviasanmateo (request):
    return render (request, 'routes/cmviasanmateo.html')

def aurora (request):
    return render (request, 'routes/aurora.html')

def smnorth (request):
    return render (request, 'routes/smnorth.html')

def smnorthviasanmateo (request):
    return render (request, 'routes/smnorthviasanmateo.html')

def qave (request):
    return render (request, 'routes/qave.html')
    # Basic validation for hour
    try:
        hour = int(hour)
    except (ValueError, TypeError):
        hour = None

    # Example route start/end points (customize as needed)
    routes_coords = {
        'litex': ("14.6901,121.0641", "14.6561,121.0306"),
        'cubao': ("14.6220,121.0500", "14.6280,121.0780"),
        'smnorth': ("14.6544,121.0419", "14.6762,121.0452"),
    }
    start, end = routes_coords.get(route, routes_coords['litex'])

    key = 'lxPgf6GPTpSWaAO9RiYCZB8egvxGmVWj'

    url = f"https://api.tomtom.com/routing/1/calculateRoute/{start}:{end}/json?key={key}&traffic=true"

    # If hour is provided, set departureTime (ISO format)
    if hour is not None:
        from datetime import datetime, timedelta
        now = datetime.now()
        departure = now.replace(hour=hour, minute=0, second=0, microsecond=0)
        # If the hour is earlier than now, assume next day
        if departure < now:
            departure += timedelta(days=1)
        departure_time = departure.isoformat() + 'Z'
        url += f"&departureTime={departure_time}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        delay = data['routes'][0]['summary'].get('trafficDelayInSeconds', 0)
        return JsonResponse({'delay_seconds': delay})
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
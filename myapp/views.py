from django.shortcuts import render

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

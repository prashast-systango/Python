from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request, 'Application1/setcookie.html')
    response.set_cookie('name', 'Prashast')
    return response

def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name', "Guest")
    return render(request, 'Application1/getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'Application1/delcookie.html')
    response.delete_cookie('name')
    return response
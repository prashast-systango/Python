from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Prashast'
    request.session['lname'] = 'Sitlani'
    return render(request, 'Application1/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default ='Guest')
    items = request.session.items()
    age = request.session.setdefault('age','22')
    return render(request, 'Application1/getsession.html', {'Name':name,'Items':items,'Age':age})

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render(request, 'Application1/delsession.html')    
   
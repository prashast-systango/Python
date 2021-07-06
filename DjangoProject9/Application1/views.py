from django.shortcuts import render

def yellow(request):
    details = {'color':"yellow",
    'flower' : "rose"}
    return render(request,'yellow.html', details)

def red(request):
    details = {'color':"red",
    'flower' : "rose"}
    return render(request,'red.html', details)

def blue(request):
    details = {'color':"blue",
    'flower' : "rose"}
    return render(request,'blue.html', details)

def black(request):
    details = {'color':"black",
    'flower' : "rose"}
    return render(request,'black.html', details)
from django.shortcuts import render, HttpResponseRedirect

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

#def organigrama(request):
#    return render(request, "core/organigrama.html")

def store(request):
    return render(request, "core/store.html")

def contact(request):
    return render(request, "core/contact.html")

def politicas(request):
    return render(request, "core/politicas.html")

def sample(request):
    return render(request, "core/sample.html")
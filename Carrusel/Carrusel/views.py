from django.shortcuts import render

# Create your views here.


def error_404(request, *args, **argv):
    Error='404'
    Text='Página no encontrada'
    return render(request, '404.html', {'Error':Error, 'Text':Text})

def error_500(request, *args, **argv):
    Error='404'
    Text='Error Interno en el Servidor'
    return render(request, '404.html', {'Error':Error, 'Text':Text})
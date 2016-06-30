from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from lib.calendar import mainCalendar
from lib.calendar import mainAnualCalendar
from lib.ehudata import mainData


@csrf_exempt
def crear_calendario(request):
    if request.method == 'GET': #Si se hace un GET se muestra solamente la vista
        return render(request, 'asignaturas/calendario.html', {})
    else: #Si es un post se crea el calendario y se envia un JSON con el fichero
        body_unicode = request.body.decode('utf-8')
        received_json_data = json.loads(body_unicode)

        data = {}
        asignaturas = []
        for asig in received_json_data["asignaturas"]:
            asignaturas.append(mainData.getHorarioAsignatura(asig))
        data["asignaturas"] = asignaturas
        calendarFile = mainCalendar.createCalendar(data, mainData.getDiasSemanas())

        #Se convierte a JSON para poder gestionarlo bien en el cliente
        calendario = {}
        calendario["calendario"] = calendarFile
        return HttpResponse(json.dumps(calendario))

# Input: User request
# Output 1: Web html solicitada por usuario
# Output 2: Descarga del calendario en el navegador del cliente
#
@csrf_exempt
def crear_calendario2(request):
    if request.method == 'GET': #Si se hace un GET se muestra solamente la vista
        return render(request, 'asignaturas/calendario.html', {})
    elif request.method == 'POST':
        #Si es un post y es el boton de "download" se crea el calendario y se envia un JSON con el fichero
        body_unicode = request.body.decode('utf-8')
        received_json_data = json.loads(body_unicode)

        calendarFile = mainAnualCalendar.crearCalendario2(received_json_data)
        print calendarFile
        #Se convierte a JSON para poder gestionarlo bien en el cliente
        return HttpResponse(json.dumps(calendarFile))

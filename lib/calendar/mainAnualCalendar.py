import datetime
from icalendar import Calendar, Event, vCalAddress, vText, vFrequency, vRecur
import json

# Input: JSON estandar de calendario
# Output: Contenido en formato iCal
#   Anade el curso academico al calendario y la fecha de creacion
#   Anade un evento por cada fecha de inicio y fin de cuatrimestre
def crearCalendario2(data):
    try:
        cal = Calendar()
        # anade al calendario el curso academico
        cal.add('prodid', data['cursoAcademico'])
        # anade a calendario la fecha de creacion
        cal.add('dtstamp', datetime.datetime.today())

        # anade los eventos de inicio y fin de cuatrimestre
        cal.add_component(nuevo_evento(data['inicioCuatrimestreUno'],data['inicioCuatrimestreUno'],'Inicio Primer Cuatrimestre'))
        cal.add_component(nuevo_evento(data['finCuatrimestreUno'],data['finCuatrimestreUno'],'Fin Primer Cuatrimestre'))
        cal.add_component(nuevo_evento(data['inicioCuatrimestreDos'],data['inicioCuatrimestreDos'],'Inicio Segundo Cuatrimestre'))
        cal.add_component(nuevo_evento(data['finCuatrimestreDos'],data['finCuatrimestreDos'],'Fin Segundo Cuatrimestre'))

        cal_content = cal.to_ical()
        return cal_content
    except Exception as e:

        print("Error al crear calendario2")
        print (str(e))


# Input: Fechas inicio y fin en formato estandar de JSON calendario "YYYY/MM/DD WED"
#         Summary descripcion texto del evento
#         Extension : Lugar del evento
# Output: Evento con parametros de entrada y UID= fecha inicio
#
def nuevo_evento(fechaInicio, fechaFin, Summary):
    # anade a calendario la fecha de fin de cuatrimestre
    try:
        event = Event()
        fechaI = fechaInicio.split(' ')[0] + " 00:00:00"
        fechaF = fechaFin.split(' ')[0] + " 23:59:59"
        event['dtstart']= formatodata(fechaI)
        event['dtend']= formatodata(fechaF)
        event['summary']= Summary
        event['uid'] = fechaI
        return event
    except Exception as e:

        print("Error al crear evento")
        print (str(e))

def formatodata(date):
    d = datetime.datetime.strptime(date,'%Y/%m/%d %H:%M:%S')
    return d.strftime('%Y%m%dT%H%M%S')#str(d.year) + str(d.month) + str(d.day) + 'T' + str(d.hour) + str(d.minute) + str(d.second)

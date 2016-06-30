from django.test import TestCase
import json
# Create your tests here.

# Estructura del json
"""
ad(data_file)

# Para cargar múltiples objetos json
data = []
with codecs.open('d:\output.txt','rU','utf-8') as f:
    for line in f:
       data.append(json.loads(line))

# Comprobación de los campos del json
ind = 0
self.assertEqual( data["Examenes"][ind]["Nombre"], )
self.assertEqual( data["Examenes"][ind]["Dia"], )
self.assertEqual( data["Examenes"][ind]["HInicio"], )
self.assertEqual( data["Examenes"][ind]["HFin"], )

self.assertEqual( data["Clases"][ind]["Dia"], )
self.assertEqual( data["Clases"][ind]["HInicio"], )
self.assertEqual( data["Clases"][ind]["HFin"], )

self.assertEqual( data["Tareas"][ind]["Titulo"], )
self.assertEqual( data["Tareas"][ind]["Descripcion"], )
self.assertEqual( data["Tareas"][ind]["HFin"], )
self.assertEqual( data["Tareas"][ind]["Creador"], )

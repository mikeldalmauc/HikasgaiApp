from django.test import TestCase
from asignaturas.models import Facultad, CursoAcademico, Asignatura
import datetime
#, CursoAcademico, Asignatura

# Create your tests here.

class FacultadTestCase(TestCase):
	def setUp(self):
		print 'Create obj'
		Facultad.objects.create(nombre="Facultad de Stormwind", universidad="Universidad publica de Mordor", direccion="Tirando pa cuenca", especialidades={'nombre': 'software'})
		
	def test_str(self):
		f = Facultad.objects.get(nombre="Facultad de Stormwind")
		self.assertEqual(str(f), f.nombre)

	def test_instance(self):
		f = Facultad.objects.get(nombre="Facultad de Stormwind")
		self.assertIsInstance(f, Facultad)
		print 'test'

	def test_nombre(self):
		f = Facultad.objects.get(nombre="Facultad de Stormwind")
		self.assertEqual(f.nombre, "Facultad de Stormwind")

	def test_universidad(self):
		f = Facultad.objects.get(nombre="Facultad de Stormwind")
		self.assertEqual(f.universidad, "Universidad publica de Mordor")

	def test_direccion(self):
		f = Facultad.objects.get(nombre="Facultad de Stormwind")
		self.assertEqual(f.direccion, "Tirando pa cuenca")

	'''def test_especialidades(self):
		f = Facultad.objects.get(nombre="Facultad de Stormwind")
		f2 = Facultad.objects.filter(especialidades__nombre='software')
		#self.assertIsInstance(f.especialidades, json)
		self.assertEqual(f, f2)'''




'''class CursoAcademicoTestCase(TestCase):
	def setUp(self):
		facultad = Facultad.objects.create(nombre="Facultad de Stormwind", universidad="Universidad publica de Mordor", direccion="Tirando pa cuenca", especialidades={'nombre': 'software'})
		CursoAcademico.objects.create(facultad=facultad)

	def test_instance_cursoacademico(self):
		curso = CursoAcademico.objects.get(facultad=(Facultad.objects.get(nombre="Facultad de Stormwind")))
		print curso
		self.assertIsInstance(curso, CursoAcademico)

	def test_iniciocuatrimestre(self):
		curso = CursoAcademico.objects.get(facultad=(Facultad.objects.get(nombre="Facultad de Stormwind")))
		self.assertIsInstance(curso.inicioCuatrimestreUno, datetime.date)		'''






class AsignaturaTestCase(TestCase):



'''

class AsignaturaAnnoTestCase(TestCase):
	pass

class ValoracionAsignaturaTestCase(TestCase):
	pass

class TareaTestCase(TestCase):

	pass

class MeGustaTareaTestCase(TestCase):
	pass

class ComentarioTestCase(TestCase):
	pass

class MeGustaComentarioTestCase(TestCase):
	pass

class LogsTestCase(TestCase):
	pass'''
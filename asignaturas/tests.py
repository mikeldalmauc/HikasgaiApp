from django.test import TestCase
from asignaturas.models import Campus, Facultad, Grado, NivelCurso, Asignatura, GrupoIdioma, DatosTemporales, Grupo, Tarea, ValoracionAsignatura, MeGustaTarea, Comentario, MeGustaComentario, Logs, SubscripcionGrupo, Matricula
import datetime
from django.contrib.auth.models import User

#=========================================
#				CAMPUS
#=========================================

class CampusTestCase(TestCase):
	def setUp(self):
		print 'Create Campus obj'
		Campus.objects.create(nombre='AR', codigo='123456789')

	def test_createdinstance(self):
		c = Campus.objects.get(nombre='AR')
		self.assertIsInstance(c, Campus)

	def test_str(self):
		c = Campus.objects.get(nombre='AR')
		self.assertEqual(str(c), c.nombre)


#=========================================
#				FACULTAD
#=========================================

class FacultadTestCase(TestCase):
	def setUp(self):
		print 'Create Facultad obj'
		c = Campus.objects.create(nombre='AR', codigo='123456789')
		Facultad.objects.create(nombre='Facultad de Stormwind', campus=c)

	def test_createdinstance(self):
		f = Facultad.objects.get(nombre="Facultad de Stormwind")
		self.assertIsInstance(f, Facultad)


	def test_str(self):
		f = Facultad.objects.get(nombre="Facultad de Stormwind")
		self.assertEqual(str(f), f.nombre)


#=========================================
#				GRADO
#=========================================

class GradoTestCase(TestCase):
	def setUp(self):
		print 'Create Grado obj'
		Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')

	def test_createdinstance(self):
		g = Grado.objects.get(pk=1)
		self.assertIsInstance(g, Grado)

	def test_str(self):
		g = Grado.objects.get(pk=1)
		self.assertEqual(str(g), g.nombre)


#=========================================
#				NIVELCURSO
#=========================================

class NivelCursoTestCase(TestCase):
	def setUp(self):
		print 'Create NivelCurso obj'
		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		NivelCurso.objects.create(curso='2022', grado=g)

	def test_createdinstance(self):
		nc = NivelCurso.objects.get(pk=1)
		self.assertIsInstance(nc, NivelCurso)

	def test_str(self):
		nc = NivelCurso.objects.get(pk=1)
		self.assertEqual(str(nc), nc.curso)


#=========================================
#				ASIGNATURA
#=========================================

class AsignaturaTestCase(TestCase):

	def setUp(self):
		print 'Create Asignatura obj'
		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		nc = NivelCurso.objects.create(curso='2022', grado=g)
		Asignatura.objects.create(codigo=420, cuatrimestre='Segundo', curso=nc)	

	def test_createdinstance(self):
		a = Asignatura.objects.get(pk=1)
		self.assertIsInstance(a, Asignatura)
		
	def test_str(self):
		a = Asignatura.objects.get(pk=1)
		self.assertEqual(a.__str__(),420)


#=========================================
#				GRUPOIDIOMA
#=========================================

class GrupoIdiomaTestCase(TestCase):
	def setUp(self):
		print 'Create GrupoIdioma obj'
		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		nc = NivelCurso.objects.create(curso='2022', grado=g)
		a = Asignatura.objects.create(codigo=420, cuatrimestre='Segundo', curso=nc)	
		GrupoIdioma.objects.create(nombreIdioma='EU', acronimoAsignatura='SGTA', nombreAsignatura='Satelak eta Grand Theft Auto', asignatura=a)

	def test_createdinstance(self):
		gi = GrupoIdioma.objects.get(pk=1)
		self.assertIsInstance(gi, GrupoIdioma)

	def test_str(self):
		gi = GrupoIdioma.objects.get(pk=1)
		self.assertEqual(str(gi), gi.acronimoAsignatura)

#=========================================
#				DATOSTEMPORALES
#=========================================

class DatosTemporalesTestCase(TestCase):
	def setUp(self):
		print 'Create DatosTemporales obj'
		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		nc = NivelCurso.objects.create(curso='2022', grado=g)
		a = Asignatura.objects.create(codigo=420, cuatrimestre='Segundo', curso=nc)	
		gi = GrupoIdioma.objects.create(nombreIdioma='EU', acronimoAsignatura='SGTA', nombreAsignatura='Satelak eta Grand Theft Auto', asignatura=a)
		DatosTemporales.objects.create(grupoIdioma=gi)

	def test_createdinstance(self):
		dt = DatosTemporales.objects.get(pk=1)
		self.assertIsInstance(dt, DatosTemporales)

	def test_str(self):
		dt = DatosTemporales.objects.get(pk=1)
		self.assertEqual(str(dt), dt.grupoIdioma.acronimoAsignatura)

#=========================================
#				GRUPO
#=========================================

class GrupoTestCase(TestCase):
	def setUp(self):
		print 'Create Grupo obj'
		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		nc = NivelCurso.objects.create(curso='2022', grado=g)
		a = Asignatura.objects.create(codigo=420, cuatrimestre='Segundo', curso=nc)	
		gi = GrupoIdioma.objects.create(nombreIdioma='EU', acronimoAsignatura='SGTA', nombreAsignatura='Satelak eta Grand Theft Auto', asignatura=a)
		dt = DatosTemporales.objects.create(grupoIdioma=gi)
		Grupo.objects.create(nombre=31, datosTemporales=dt)

	def test_createdinstance(self):
		g = Grupo.objects.get(pk=1)
		self.assertIsInstance(g, Grupo)
		
	def test_str(self):
		g = Grupo.objects.get(pk=1)
		self.assertEqual(str(g), str(g.nombre))


#=========================================
#				TAREA
#=========================================

class TareaTestClase(TestCase):
	def setUp(self):
		print 'Create Tarea obj'
		user = User.objects.create_user(username='Fofrito', password='ikdislife', email='satelnitxok@evangelion.eus')

		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		nc = NivelCurso.objects.create(curso='2022', grado=g)
		a = Asignatura.objects.create(codigo=420, cuatrimestre='Segundo', curso=nc)	
		gi = GrupoIdioma.objects.create(nombreIdioma='EU', acronimoAsignatura='SGTA', nombreAsignatura='Satelak eta Grand Theft Auto', asignatura=a)
		dt = DatosTemporales.objects.create(grupoIdioma=gi)
		grupo = Grupo.objects.create(nombre=31, datosTemporales=dt)
		Tarea.objects.create(descripcion='Cata de vino en la destileria Mendixabal', titulo='aventura enologa', hora='12:00:00', puntuacion=10, grupo=grupo, autor=user)


	def test_createdinstance(self):
		t = Tarea.objects.get(pk=1)
		self.assertIsInstance(t, Tarea)
		
	def test_str(self):
		t = Tarea.objects.get(pk=1)
		self.assertEqual(str(t), t.titulo)


#=========================================
#			VALORACIONASIGNATURA
#=========================================

class ValoracionAsignaturaTestCase(TestCase):
	def setUp(self):
		print 'Create ValoracionAsignatura obj'

		user = User.objects.create_user(username='Jordi Hurtado', password='ironman9000', email='noseprogramar@aguringlaterra.com')

		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		nc = NivelCurso.objects.create(curso='2022', grado=g)
		a = Asignatura.objects.create(codigo=420, cuatrimestre='Segundo', curso=nc)	

		ValoracionAsignatura.objects.create(valoracion=10, argumento='Dulcisimo, a LIDL', asignatura=a, autor=user)


	def test_createdinstance(self):
		va = ValoracionAsignatura.objects.get(pk=1)
		self.assertIsInstance(va, ValoracionAsignatura)
		
	def test_str(self):
		va = ValoracionAsignatura.objects.get(pk=1)
		self.assertEqual(str(va),'1')


#=========================================
#				MEGUSTATAREA
#=========================================

class MeGustaTareaTestCase(TestCase):

	def setUp(self):
		print 'Create MeGustaTarea obj'
		user = User.objects.create_user(username='1234', password='adminadmin', email='google@google.goo')

		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		nc = NivelCurso.objects.create(curso='2022', grado=g)
		a = Asignatura.objects.create(codigo=420, cuatrimestre='Segundo', curso=nc)	
		gi = GrupoIdioma.objects.create(nombreIdioma='EU', acronimoAsignatura='SGTA', nombreAsignatura='Satelak eta Grand Theft Auto', asignatura=a)
		dt = DatosTemporales.objects.create(grupoIdioma=gi)
		grupo = Grupo.objects.create(nombre=31, datosTemporales=dt)
		t = Tarea.objects.create(descripcion='Cata de vino en la destileria Mendixabal', titulo='aventura enologa', hora='12:00:00', puntuacion=10, grupo=grupo, autor=user)

		MeGustaTarea.objects.create(valor=1, autor=user, tarea=t)

	def test_createdinstance(self):
		mgt = MeGustaTarea.objects.get(pk=1)
		self.assertIsInstance(mgt, MeGustaTarea)

	def test_str(self):
		mgt = MeGustaTarea.objects.get(pk=1)
		self.assertEqual(str(mgt), mgt.tarea.titulo)


#=========================================
#				COMENTARIO
#=========================================

class ComentarioTestCase(TestCase):

	def setUp(self):

		print 'Create Comentario obj'
		user = User.objects.create_user(username='1234', password='adminadmin', email='google@google.goo')

		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		nc = NivelCurso.objects.create(curso='2022', grado=g)
		a = Asignatura.objects.create(codigo=420, cuatrimestre='Segundo', curso=nc)	
		gi = GrupoIdioma.objects.create(nombreIdioma='EU', acronimoAsignatura='SGTA', nombreAsignatura='Satelak eta Grand Theft Auto', asignatura=a)
		
		Comentario.objects.create(contenido='ey b0ss', puntuacion=3, autor=user, grupoIdioma=gi)

	def test_createdinstance(self):
		c = Comentario.objects.get(pk=1)
		self.assertIsInstance(c, Comentario)

	def test_str(self):
		c = Comentario.objects.get(pk=1)
		self.assertEqual(str(c),c.autor.username)

#=========================================
#			 MEGUSTACOMENTARIO
#=========================================


class MeGustaComentarioTestCase(TestCase):

	def setUp(self):
		print 'Create MeGustaComentario obj'
		user = User.objects.create_user(username='1234', password='adminadmin', email='google@google.goo')
		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		nc = NivelCurso.objects.create(curso='2022', grado=g)
		a = Asignatura.objects.create(codigo=420, cuatrimestre='Segundo', curso=nc)	
		gi = GrupoIdioma.objects.create(nombreIdioma='EU', acronimoAsignatura='SGTA', nombreAsignatura='Satelak eta Grand Theft Auto', asignatura=a)
		c = Comentario.objects.create(contenido='ey b0ss', puntuacion=3, autor=user, grupoIdioma=gi)
		MeGustaComentario.objects.create(valor=1, autor=user, comentario=c)

	def test_createdinstance(self):
		mgc = MeGustaComentario.objects.get(pk=1)
		self.assertIsInstance(mgc, MeGustaComentario)

	def test_str(self):
		mgc = MeGustaComentario.objects.get(pk=1)
		self.assertEqual(str(mgc), str(mgc.comentario))

#=========================================
#			 		LOGS
#=========================================

class LogsTestCase(TestCase):

	def setUp(self):
		user = User.objects.create_user(username='1234', password='adminadmin', email='google@google.goo')
		g = Grado.objects.create(nombre='Ingenieria de catapultas', codigo='geass')
		Logs.objects.create(data='Ey que pasa, soy un string de django, soy especial y no compilo si me pones una maldita tilde', grado=g, usuario=user)

	def test_createdinstance(self):
		log = Logs.objects.get(pk=1)
		self.assertIsInstance(log, Logs)

	def test_str(self):
		log = Logs.objects.get(pk=1)
		self.assertEqual(str(log), log.grado.nombre)



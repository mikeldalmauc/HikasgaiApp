from django.test import TestCase
from asignaturas.models import Facultad, CursoAcademico, Asignatura, AsignaturaAnno, ValoracionAsignatura, Tarea, MeGustaTarea, Comentario, MeGustaComentario, Logs
import datetime
from django.contrib.auth.models import User
#, CursoAcademico, Asignatura

# Create your tests here.

class FacultadTestCase(TestCase):
	def setUp(self):
		print 'Create obj'
		Facultad.objects.create(nombre="Facultad de Stormwind", universidad="Universidad publica de Mordor", direccion="Tirando pa cuenca", especialidades={'nombre': 'software'})
		

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
		self.assertIsInstance(f.especialidades, JsonModel)
		self.assertEqual(f, f2)'''

	def test_str(self):
		f = Facultad.objects.get(nombre="Facultad de Stormwind")
		self.assertEqual(str(f), f.nombre)




'''class CursoAcademicoTestCase(TestCase):
	def setUp(self):
		fac = Facultad.objects.create(nombre="Facultad de Stormwind", universidad="Universidad publica de Mordor", direccion="Tirando pa cuenca", especialidades={'nombre': 'software'})
		CursoAcademico.objects.create(facultad=fac)

	def test_instance_cursoacademico(self):
		curso = CursoAcademico.objects.get(facultad=(Facultad.objects.get(nombre="Facultad de Stormwind")))
		print curso
		self.assertIsInstance(curso, CursoAcademico)

	def test_iniciocuatrimestre(self):
		curso = CursoAcademico.objects.get(facultad=(Facultad.objects.get(nombre="Facultad de Stormwind")))
		self.assertIsInstance(curso.inicioCuatrimestreUno, datetime.date)'''		


class AsignaturaTestCase(TestCase):

	def setUp(self):
		Asignatura.objects.create(nombre='AEA', codigo=100, nombreCompleto='Aplicaciones de la esgrima avanzada', curso='3', idioma='es')
		Asignatura.objects.create(nombre='BPF', codigo=200, nombreCompleto='Barbacoa para familias', curso='3', idioma='es')

	def test_createdinstance(self):
		a = Asignatura.objects.get(nombre='AEA')
		b = Asignatura.objects.get(nombre='BPF')
		self.assertIsInstance(a, Asignatura)
		self.assertNotEqual(a,b)
		
	def test_str(self):
		a = Asignatura.objects.get(codigo=200)
		self.assertEqual(str(a),"BPF")


'''class AsignaturaAnnoTestCase(TestCase):
	def setUp(self):
		asign = Asignatura.objects.create(nombre='BPF', codigo=200, nombreCompleto='Barbacoa para familias', curso='3', idioma='es')
		AsignaturaAnno.objects.create(plazasSolicitadas=100, anno=1995,creditosMinimos=120,plazasOcupadas=10, plazasMaximas=120, cuatrimestre='1', diaHorarioAgrupado='L', descripcion='Hola', asignatura=asign)

	def test_createdinstance(self):
		a = AsignaturaAnno.objects.get(pk=1)
		self.assertIsInstance(a.asignatura, Asignatura)
		self.assertIsInstance(a, AsignaturaAnno)

	def test_str(self):
		a = AsignaturaAnno.objects.get(pk=1)
		self.assertEqual(str(a), a.asignatura.nombre)'''


'''class ValoracionAsignaturaTestCase(TestCase):
	def setUp(self):
		u=User.objects.create_user(username='peru', password='adminadmin123', email='peru@peru.per')
		asign = Asignatura.objects.create(nombre='BPF', codigo=200, nombreCompleto='Barbacoa para familias', curso='3', idioma='es')
		asign_anno = AsignaturaAnno.objects.create(plazasSolicitadas=100, anno=1995,creditosMinimos=120,plazasOcupadas=10, plazasMaximas=120, cuatrimestre='1', diaHorarioAgrupado='L', descripcion='Hola', asignatura=asign)
		ValoracionAsignatura.objects.create(valoracion=10, argumento='Yes', asignatura=asign_anno, creador=u)
		'''


class TareaTestCase(TestCase):
	def setUp(self):
		u = User.objects.create_user(username='peru', password='adminadmin123', email='peru@peru.per')
		Tarea.objects.create(descripcion='...', titulo='Examen', HFin='14:00:00', HInicio='12:00:10', puntuacion=10, creador=u)

	def test_createdinstance(self):
		tarea = Tarea.objects.get(pk=1)
		self.assertIsInstance(tarea, Tarea)

	def test_str(self):
		tarea = Tarea.objects.get(pk=1)
		self.assertEqual(str(tarea), tarea.titulo)


class MeGustaTareaTestCase(TestCase):
	def setUp(self):
		u = User.objects.create_user(username='LordUmami1337', password='actofseasoning', email='gladyoucould@bake.it')
		tar = Tarea.objects.create(descripcion='...', titulo='Examen', HFin='14:00:00', HInicio='12:00:10', puntuacion=10, creador=u)
		mgt = MeGustaTarea.objects.create(valor=1,valorador=u,tarea=tar)

	def test_createdinstance(self):
		mgt = MeGustaTarea.objects.get(valor=1)
		self.assertIsInstance(mgt, MeGustaTarea)

	def test_str(self):
		mgt = MeGustaTarea.objects.get(valor=1)
		self.assertEqual(str(mgt), mgt.tarea.titulo)
	

class ComentarioTestCase(TestCase):
	def setUp(self):
		u = User.objects.create_user(username='KingArthas69', password='frostmourne420', email='lichking@deathknight.wow')
		Comentario.objects.create(contenido='JAJAJJ K BUENA TU XDXDXDXDXD LE DEJO MIS DIESES NOMAS', creador=u)

	def test_createdinstance(self):
		com = Comentario.objects.get(pk=1)
		self.assertIsInstance(com, Comentario)

	def test_str(self):
		com = Comentario.objects.get(pk=1)
		self.assertEqual(str(com), com.contenido)

class MeGustaComentarioTestCase(TestCase):
	def setUp(self):
		u = User.objects.create_user(username='KingArthas69', password='frostmourne420', email='lichking@deathknight.wow')
		c = Comentario.objects.create(contenido='JAJAJJ K BUENA TU XDXDXDXDXD LE DEJO MIS DIESES NOMAS', creador=u)
		MeGustaComentario.objects.create(valor=1, valorador=u, comentario=c)

	def test_createdinstance(self):
		mgc = MeGustaComentario.objects.get(pk=1)
		self.assertIsInstance(mgc, MeGustaComentario)	

class LogsTestCase(TestCase):
	pass'''
from django.test import TestCase
from usuarios.models import Perfil, Profesor, Alumno, ContactoWeb
from django.contrib.auth.models import User
import datetime

#TESTS DE MODELO: Perfil

class PerfilTestCase(TestCase):
	def setUp(self):
		user = User.objects.create_user(username='david', email='helloworld@gmail.com', password='password')
		Perfil.objects.create(usuario=user, genero="F", nacimiento="2009-10-03", fechaRegistro="2009-10-03", karma=50, rango="N")

		user2 = User.objects.create_user(username='hayter', email='helloworld2@gmail.com', password='password')
		Perfil.objects.create(usuario=user2, genero='M', nacimiento="2009-10-11", fechaRegistro="2009-10-11", karma=50, rango="N")

	def test_instancia(self):
		perfil = Perfil.objects.get(usuario=User.objects.get(username="david"))
		self.assertIsInstance(perfil, Perfil)

	def test_usuario(self):
		perfil = Perfil.objects.get(usuario=User.objects.get(username="david"))
		self.assertIsInstance(perfil.usuario, User)
		self.assertEqual(perfil.usuario.username, str(perfil))

	def test_genero(self):
		perfil = Perfil.objects.get(usuario=User.objects.get(username="david"))
		self.assertIn(perfil.genero, ("F", "M", "Masculino", "Femenino"))

	def test_nacimiento(self):
		perfil = Perfil.objects.get(usuario=User.objects.get(username="david"))
		self.assertIsInstance(perfil.nacimiento, datetime.date)	
		
	def test_avatar(self):
		pass

	def test_fechaRegistro(self):
		perfil = Perfil.objects.get(usuario=User.objects.get(username="david"))
		self.assertIsInstance(perfil.fechaRegistro, datetime.date)	

	def test_karma(self):
		perfil = Perfil.objects.get(usuario=User.objects.get(username="david"))
		self.assertIsInstance(perfil.karma, int)

	def test_rango(self):
		perfil = Perfil.objects.get(usuario=User.objects.get(username="david"))
		self.assertIn(perfil.rango,('N','Novato','E','Estudiante','B','Becario','P','Pelota'))

	def test_cuentaGmail(self):
		pass

	def test_str(self):
		perfil = Perfil.objects.get(usuario=User.objects.get(username="david"))
		self.assertEqual(str(perfil), perfil.usuario.username)



#TESTS DE MODELO: Profesor

class ProfesorTestCase(TestCase):
	def setUp(self):
		user = User.objects.create_user(username='xabin', email='graeh@euskaltel.net', password='password')
		Profesor.objects.create(usuario=user, genero='M', nacimiento='1996-05-15', rango='B', despacho=107)
		

	def test_instancia(self):
		profesor1=Profesor.objects.get(usuario=User.objects.get(username='xabin'))
		self.assertIsInstance(profesor1, Profesor)

	def test_despacho(self):
		profesor1=Profesor.objects.get(usuario=User.objects.get(username='xabin'))
		self.assertIsInstance(profesor1.despacho, int)
		self.assertEqual(107, profesor1.despacho)

class AlumnoTestCase(TestCase):
	def setUp(self):
		user = User.objects.create_user(username='arlet', email='graeh@euskaltel.net', password='password')
		Alumno.objects.create(usuario=user, genero='M', nacimiento='1996-05-15', rango='B', creditos=2, notaMedia=7.5, curso=3, especialidad="Hardware")

	def test_instancia(self):
		alumno = Alumno.objects.get(usuario=User.objects.get(username="arlet"))
		self.assertIsInstance(alumno,Alumno)

	def test_creditos(self):
		alumno = Alumno.objects.get(usuario=User.objects.get(username="arlet"))
		self.assertIsInstance(alumno.creditos, int)
		self.assertEqual(alumno.creditos, 2)
	def test_notaMedia(self):
		alumno = Alumno.objects.get(usuario=User.objects.get(username="arlet"))
		self.assertIsInstance(alumno.notaMedia, float)
		self.assertEqual(7.5, alumno.notaMedia)

	def test_curso(self):
		alumno = Alumno.objects.get(usuario=User.objects.get(username="arlet"))
		self.assertIn(alumno.curso, ('1','2','3','4','5','Primero','Segundo','Tercero','Cuarto','Quinto'))

	def test_especialidad(self):
		alumno = Alumno.objects.get(usuario=User.objects.get(username="arlet"))
		self.assertIsInstance(alumno.especialidad, basestring)


class ContactoWebTestCase(TestCase):
	def setUp(self):
		user = User.objects.create_user(username='arlet', email='graeh@euskaltel.net', password='password')
		ContactoWeb.objects.create(nombre="Porrusald", url='http://xvideos.com', usuario=user)
		print user.username

	def test_instancia(self):
		cweb = ContactoWeb.objects.get(usuario=User.objects.get(username='arlet'))
		self.assertIsInstance(cweb, ContactoWeb)

	def test_nombre(self):
		cweb = ContactoWeb.objects.get(usuario=User.objects.get(username='arlet'))
		self.assertIsInstance(cweb.nombre, basestring)
		self.assertEqual(cweb.nombre,str(cweb.nombre))

	def test_url(self):
		pass
		#cweb = ContactoWeb.objects.get(usuario=User.objects.get(username='arlet'))

	def test_usuario(self):
		cweb = ContactoWeb.objects.get(usuario=User.objects.get(username='arlet'))
		self.assertIsInstance(cweb.usuario, User)


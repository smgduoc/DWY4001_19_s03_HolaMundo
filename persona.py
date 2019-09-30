#°/usr/bin/python3

#vamos a definir una clase, como  las de Java
#las clases parten con MAYÚSCULA y usan camel (mayuscula por cada nueva palabra)
#[Ej clase incorrecta  alumno_duoc]			[Ej clase correcta AlumnoDuoc]

#las funciones usan minúsculas y se conectan
#con underscore
#[Ej funcion incorrecta  imprimirDetalle]		[Ej funcion correcta  imprimir_detalle]
class Persona:

	#en python hay un solo constructor llamado __init__
	#el cual debe recibir un parametro self
	# -		-		-		-		-		-
	#si una variable parte con ( _ ) underscore se debe
	#tratar como si fuera privada-  NO TOCAR
	
	def __init__(self, nombre, rut):
		self._nombre = nombre
		self.rut = rut
		

	def imprimir(self):
		texto = " ".join(("Soy: ", self._nombre , "y mi rut es: ", self.rut))
		print(texto)
# ahora el "main" , que está fuera de la clase
perrin = Persona("Juan Eduardo", "1237745-3")
perrin.imprimir()

#en python los atributos son publicos
#y se pueden modificcar directamnte

perrin.rut= "1237745-3"
perrin.imprimir()

#crear una persona leyendo desde la consola
nombre = input("Ingresar nombre: ")
rut = input("Ingresar RUT: ")
personaIngresada = Persona(nombre, rut)
personaIngresada.imprimir()

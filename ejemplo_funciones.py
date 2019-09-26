#!/usr/bin/python3

#guardar en la carpeta del proyecto
# X:\laragon\www\DWY4001_19_s03_HolaMundo
# con el nombre ejemplo_funciones.py


def funcion_tonta(nombre):
	separador = " "
	mensaje = separador.join(("Ah", "El inoperante de:" , nombre))
	print(mensaje)
	
#llamo a la funcion
funcion_tonta("Ian") 
funcion_tonta("Gatocrack")


#calculo del DV de un rut

def digito_verificador(rut):
	digito =""
	contador =2
	suma =0
	multiplo =0
	while rut > 0:
		multiplo = (rut % 10) * contador
		suma = suma + multiplo
		rut = rut // 10 #division entera
		contador = contador + 1
		if contador == 8:
			contador =2
	digito = 11 - (suma % 11)
	if digito == 10:
		digito = 'k'
	if digito == 11:
		digito = 0
	return str(digito)
	
	
digito_verificador(19689892)

mi_rut = 19689892
print("-".join((str(mi_rut), digito_verificador(mi_rut))))

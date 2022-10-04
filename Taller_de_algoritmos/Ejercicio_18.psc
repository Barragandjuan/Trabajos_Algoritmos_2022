// Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 18
Algoritmo Inicio_primeras_letras
	//Entradas nombre, Primer apellido, Segundo apellido
	Escribir "Digite su nombre: "
	Leer Nombre
	Escribir "Digite su primer apellido: "
	Leer primer_Apellido
	Escribir "Digite su segundo apellido: "
	Leer segundo_Apellido
	//Caja Negra
	n<-SubCadena(Nombre,1,1)
	ap1<-Subcadena(primer_Apellido,1,1)
	ap2<-Subcadena(segundo_Apellido,1,1)
	//Salida
	Escribir "Las iniciales son: " n ap1 ap2
FinAlgoritmo

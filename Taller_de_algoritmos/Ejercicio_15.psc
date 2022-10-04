// Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 15
Algoritmo Inicio_Invertir_Numero
	//Entrada numero
	Escribir "Digite el numero a invertir: "
	Leer numero1
	//caja negra
	u<- numero1 MOD 10
	d<-trunc(numero1/10)
	//Salida Numero Invertido
	Escribir "El valor del numero invertido es: " u d
FinAlgoritmo

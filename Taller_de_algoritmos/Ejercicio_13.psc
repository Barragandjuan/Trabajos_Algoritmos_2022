// Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 13
Algoritmo Inicio_Ubicacion
	//Entradas
	Escribir "Digite el valor de x1: "
	Leer x1
	Escribir "Digite el valor de y1: "
	Leer y1
	Escribir "Digite el valor de x2: "
	Leer x2
	Escribir "Digite el valor de y2: "
	Leer y2
	//Caja negra
	op1<-(x2-x1)^2
	op2<-(y2-y1)^2
	d<-raiz(op1+op2)
	//Salida
	Escribir "El valor de la distancia es: " d
FinAlgoritmo

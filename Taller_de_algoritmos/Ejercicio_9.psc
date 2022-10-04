// Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 9
Algoritmo Inicio_comisiones
	//Entradas
	Escribir "Digite su sueldo base: "
	Leer sueldo_Base
	Escribir "Digite las ventas realizadas este mes: "
	Leer ventas
	//Caja Negra
	comisiones<-(sueldo_Base*0.1)*ventas
	sueldoF<-sueldo_Base+comisiones
	//Salidas
	Escribir "El dinero generado por comisiones es de: " comisiones
	Escribir "Su sueldo base mas comisiones es de: " sueldoF
	
FinAlgoritmo

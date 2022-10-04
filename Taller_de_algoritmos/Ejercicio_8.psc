// Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 8
Algoritmo Inicio_conversion_minutos
	//Entrada minutos
	Escribir "Digite los minutos a convertir: "
	Leer minutos
	//Caja negra
	h<-trunc(minutos/60)
	m<-((minutos/60)-h)*60
	//Salida
	Escribir minutos " minutos son: " h " horas y " m " minutos"
FinAlgoritmo

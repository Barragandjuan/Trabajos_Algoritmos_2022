// Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 11
Algoritmo Inicio_Calificaciones
	//Entradas
	Escribir "Digite la nota de sus 3 notas parciales: "
	Leer notasP
	Escribir "Digite la nota de su examen final: "
	Leer examen
	Escribir "Digite la nota del trabajo final: "
	Leer trabajoF
	//Caja Negra
	pNotasP<-(notasP*0.55)
	pExamen<-(examen*0.30)
	pTrabajoF<-(trabajoF*0.15)
	notaF<-(pNotasP+pExamen+pTrabajoF)
	//Salidas
	Escribir "Su nota final es de: " notaF
FinAlgoritmo

# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 4

"""
Una empresa quiere hacer una compra de varias piezas de la misma clase a un fabricante de refacciones. 
La empresa dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante. 
Si el monto total de la compra excede de  $5.000.000  COP  la  empresa  tendrá  la  capacidad  de  invertir  de  su  propio 
dinero  un 5 5 % del monto de la compra, pedir presta al banco un 30% y el resto lo 
pagará  solicitando  un  crédito  al  fabricante.  Si  el  monto  total  de  la  compra  no 
excede  de $5.000.000 COP la empresa tendrá capacidad de invertir de su propio 
dinero  un  70%  y  el  restante  30%  lo  pagará  solicitando  crédito  al  fabricante.  El 
fabricante  cobra  por  concepto  de  intereses  un  20%  sobre  la  cantidad  que  se  le 
pague  a  crédito.  Calcule  y  muestre  la  cantidad  a  invertir  de  los  fondos  de  la 
empresa,  la  cantidad  a  pagar  a  crédito,  el  monto  a  pagar  por  intereses  y  si  es 
necesario, la cantidad prestada al banco.
"""
#Entrada
inversion= float(input("Ingrese el valor de la inversion a realizar: "))
#Caja Negra
if(inversion>5000000):
    contado= inversion*0.55
    prestamo_banco= inversion*0.30
    interes_banco1= float(input("Ingrese el porcentaje del valor de los intereses del banco: "))
    interes_banco2= (prestamo_banco*interes_banco1)/100
    credito1= inversion*0.15
    creditof= credito1*0.2
    pagof= contado+prestamo_banco+interes_banco2+credito1+creditof
    print("El valor final a pagar es de:",pagof)
else:
    contado= inversion*0.7
    credito1= inversion*0.3
    creditof= credito1*0.2
    pagof= contado+credito1+creditof
    print("El valor final a pagar es de:",pagof)
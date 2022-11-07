# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 8

#https://www.urionlinejudge.com.br/judge/es/problems/view/1114

senha= 2002
while True:
    senha1= int(input())
    if(senha1==senha):
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
diccionario= {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5} 
lista=[]
lista2=[]
for i in diccionario:
    lista.append(diccionario[i])

for i in lista:
    if i not in lista2:
        lista2.append(i)
print(lista2)
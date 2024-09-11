print("Ejemplo de Diccionarios")
listadenombres={
    "Nombre:": "Angel Tadeo",
    "Genero:": "Hombre",
    "Edad:": 16
}
print(listadenombres)
print("Lista de elementos del diccionario listadenombres loop for")
for DeLeon in listadenombres:
    print(DeLeon)
print("Lista de valores del diccionario listadenombres loop for")
for DeLeon in listadenombres:
    print(listadenombres[DeLeon])
print("Lista de elementos y valores del diccionario listadenombres loop for")
for x, y in listadenombres.items():
  print(x, y)
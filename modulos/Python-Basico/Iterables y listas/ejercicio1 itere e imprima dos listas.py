#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño
# al mismo tiempo.
#Ejemplos:
#first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]
#second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’] ->

first_list =  [
    "producto",
    "arroz", 
    "frijoles",
    "azucar"
]
second_list =  [
    "costo",
    "1900",
    "1100",
    "2000"
]

for product in range(len(first_list)):
    print (f'{first_list[product]}, {second_list[product]}')



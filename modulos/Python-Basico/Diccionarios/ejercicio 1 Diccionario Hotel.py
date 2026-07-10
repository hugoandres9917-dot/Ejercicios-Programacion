#Cree un diccionario que guarde la siguiente información sobre un hotel:
    #nombre
    #numero_de_estrellas
    #habitaciones
#El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
    #numero
    #piso
    #precio_por_noche

hotel ={
    'name':'Arrecife_hotel',
    'number_of_stars': 5,
    'rooms': [
    {
    'number': 1,
    'floor': 2,
    'price_per_night': 90.00,
    },
    {
	'number': 2,
    'floor': 2,
    'price_per_night': 90.00,
	},
    {
    'number': 3,
    'floor': 2,
    'price_per_night': 110.00,
    },
    {
	'number': 4,
    'floor': 2,
    'price_per_night': 110.00,
	},
],

}
print(hotel)


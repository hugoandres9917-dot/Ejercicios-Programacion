
Descripcion General de la API

PokeAPI es una API publica y gratuita la cual nos ofrece informacion sobre el universo Pokemon
puedes consultar datos de los pokemones: como sus habilidades tipos, movimientos y mas . no requiere autenticacion

2. Explicacion de cada solicitud

1. Get - obtener a pikachu

    metodo HTTP: Get

    Endpoint: https://pokeapi.co/api/v2/pokemon/pikachu
    parametros:

        pikachu: busca todo lo relacionado con este nombre

    descripcion de la respuesta: nos regresa todo la informacion de este pokemon, habilidades, estadiditicas y  URL de detalle.

    {
    "abilities": [
        {
            "ability": {
                "name": "static",
                "url": "https://pokeapi.co/api/v2/ability/9/"
            },
            "is_hidden": false,
            "slot": 1
        },
        {
            "ability": {
                "name": "lightning-rod",
                "url": "https://pokeapi.co/api/v2/ability/31/"
            },
            "is_hidden": true,
            "slot": 3
        }
    ],
    "base_experience": 112,
    "cries": {
        "latest": "https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/latest/25.ogg",
        "legacy": "https://raw.githubusercontent.com/PokeAPI/cries/main/cries/pokemon/legacy/25.ogg"
    },
    "forms": [
        {
            "name": "pikachu",
            "url": "https://pokeapi.co/api/v2/pokemon-form/25/"
        }
    ],


POST - SIMULACION DE CREACION DE RECURSO 

Esta API no permite crear recursos pero podemos hacer una simulacion con echo 

EndPoint: https://postman-echo.com/post

Body JSON

{
  "trainer": "Ash",
  "pokemon": "Pikachu"
}
Descripción de la respuesta: Devuelve el mismo JSON enviado, confirmando la creación simulada


PUT - SIMULACION DE ACTUALIZACION


EndPoint: https://postman-echo.com/put
Body (JSON)

{
  "trainer": "Ash",
  "pokemon": "Charizard"
}
Descripción de la respuesta: Devuelve el JSON actualizado, simulando la modificación de un recurso


DELETE - SIMULACION DE ELIMINACION

EndPoint: https://postman-echo.com/delete
Body (JSON)

{
  "trainer": "Ash",
  "pokemon": "Bulbasaur"
}
Descripción de la respuesta: Devuelve el JSON enviado, confirmando la eliminación simulada.

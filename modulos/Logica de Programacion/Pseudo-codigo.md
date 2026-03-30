
Ejercicios pseudocodigo

1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
    1. Si el precio es menor a 100, el descuento es del 2%.
    2. Si el precio es mayor o igual a 100, el descuento es del 10%.
    3. *Ejemplos*:
    4. 120 → 108
    5. 40 → 39.2

RESPUESTA:

1.Inicio

2.Definir `precio_de_producto`

3.Definir `descuesto`

4.Definir `precio_total`

5.Mostrar “Ingrese precio del producto”

7.Si (`precio_de_producto` ≤ 100) entonces:

    ¡.descuesto` = `precio_de_producto` * 0.02

6.Pedir `precio_de_producto`

8.Sino:

    1.Si (`precio_de_producto`  ≥ 100) entonces:

        ¡¡.descuesto` = `precio_de_producto` * 0.1

9.FinSi

10.precio_total` = `precio_de_producto` - `descuesto`

11.Mostrar “ El precio del producto con descuesto es de”

12.Mostrar `precio_total`

13.Fin


ejercicio 2

 Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “*Mayor*”. Si es exactamente igual, muestre “*Igual*”.
    1. *Ejemplos*:
        1. 1040 → Mayor
        2. 140 → 460
        3. 600 → Igual
        4. 599 → 1
    
    RESPUESTA:
    
    1.Inicio
    
    2.Definir `tiempo_en_segundos`
    
    3.Definir `10_minutos`
    
    4.Definir `resultado`
    
    5.Mostrar “ indique los segundos de la hora en este momento “
    
    6.Pedir `tiempo_en_segundos` 
    
    7. 10_minutos = 10*60
    
    8.Si ( `tiempo_en_segundos` **<** `10_minutos`) entonces:
    
        ¡.resultado` = ****`10_minutos`  -`tiempo_en_segundoso`
    
    ¡   ¡.Mostrar “ segundos faltantes para  10 minutos”.
    
        ¡¡¡.Mostrar `resultado`
    
    9.Sino:
    
        ¡.Si (`tiempo_en_segundos` **>**  `10_minutos`) entonces:
    
            a.Mostrar “Es Mayor a 10 minutos”
    
    ¡¡.SIno:
    
        a.tiempo_en_segundos` == `10_minutos`
    
        b.Mostrar “ Es igual a 10 minutos”.
    
    10.FinSi
    
    11.Fin

    Ejerecicio 3 
    1. Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
    1. 5 → 15 (1 + 2 + 3 + 4 + 5)
    2. 3 → 6 (1 + 2 + 3)
    3. 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

Respuesta:

1.Inicio 

2.Definir `numero`

3.Definir `contador`

4.Definir `resultado`

5.Mostrar “Ahora digite el numero hasta el cual quiere sumar:”

6.Pedir `numero`

7.contador = 1

9.`resultado` = 0 

10.Mientras que ( `contador`  ≤ `numero`) hacer:

    ¡.`resultado` = `resultado` + `contador`

    ¡¡.contador` = `contador`+1

11.FinMientras

12. Mostrar “ el resultado de la suma de cada numero del 1 hasta ese número que usted ingreso es de”

13.Mostrar `resultado`

14.Mostrar

15.Fin
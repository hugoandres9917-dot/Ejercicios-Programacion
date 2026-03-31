Ejerecicios extra pseudocodigo 

**Ejercicios Extra**

1. Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (`primero` y `segundo`) y los ordene de menor a mayor en dichas variables.
    1. Ejemplos:
        1. A: 56, B: 32 → A: 32, B: 56
        2. A: 24, B: 76 → A: 24, B: 76
        3. A: 45, B: 12 → A: 12, B: 45


1.Inicio

2.Definir `numero 1`

3.Definir `numero 2` 

4.Mostrar “ ingrese numero 1”

5.Pedir `numero 1`

6.Mostrar “ingrese numero 2”

7.Pedir `numero 2`

8.`numero 1` = 0

9.`numero 2` = 0

10.Si `numero 1` > `numero 2` 

    ¡.`numero 1 , numero 2` = `numero 2 , numero 1`

        a. Mostrar “ numero ordenados”

        b. Mostrar “numero 1 : primero”

        c. Mostrar “ numero 2 : segundo”

11.Finsi

12.Fin

ejercicio extra 2

2. Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que `1 km == 1000m` y `1 hora == 60 minutos * 60 segundos`.
    1. *Ejemplos*:
        1. 73 → 20.27
        2. 50 → 13.88
        3. 120 → 33.33

1.inicio

2.Definir velocidad kmh

3.Definir velocidad ms

4.mostrar “ ingrese la velocidad en km/h”

5.pedir velocidad km/h

6velocidad km/h = 0

7.velocidad ms = (velociada kmh * 1000) / 3600

8.Mostrar “ velocidad kmh” + km/h es igual “ velocidad ms “+ m/s.

9.fin

3. Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.
    1. *Ejemplos*:
        1. 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
        2. 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
        3. 1, 1, 1, 1, 1, 2 → 83.3% mujeres y 16.6% hombres
        
    
    1.inicio
    
    2.Definir mujer = 0
    
    3.Definir hombre = 0
    
    4.mientras que sexo en el rango de 6 
    
    5.mostrar “ingrese el sexo de la persona 1. para mujer , 2. para Hombre”
    
    6.Si sexo = 1
    
        mujer += 1
    
    7.sino
    
        si sexo = 2
    
            hombre += 1
    
          sino
    
    8.mostrar “ entrada invalida. por favor ingrese 1 o 2.”
    
    9.finsi
    
    10.finsi
    
    11.finmientras
    
    12.porecentanje_mujeres = (mujere / 6) * 100
    
    13.porcentanje_hombres + (hombre / 6)  * 100
    
    14.mostrar “ porcentaje de mujeres :”
    
    15.mostrar porcentaje_mujeres
    
    16.mostrar “porecentaje de hombres:”
    
    17.mostrar porcenteje_hombres
    
    18.fin
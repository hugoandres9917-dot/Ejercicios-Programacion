print("--Tabla de multiplicar personalizada--")

number = int(input("Digite un numero del 1 al 10 para mostrar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {number}:")
for i in range(1, 13):
     result = number * i
     print(f"{number} x {i} = {result}")



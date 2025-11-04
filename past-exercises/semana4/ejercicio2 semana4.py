name = input("ingrese su nombre")
last_name = input("ingrese su apellido")
age = int(input("ingrese su edad"))
if ( age <= 0 ):
    age_cathegory = "edad no vaida"
elif(age <= 1 ):
   age_cathegory = "Es un bebe "
elif(age <= 6):
    age_cathegory = "es un nino"
elif(age <= 13):
   age_cathegory = "es un preadolecente"
elif(age <= 17):
    age_cathegory = "es un adolecente"
elif(age <= 25):
    age_cathegory = "es un adulto joven"
elif(age <= 64):
   age_cathegory = "es un adulto"
else:
    age_cathegory = "eres un adulto mayor"

print(f'su nombre completo es {name}{last_name} su edad es {age} por ende usted {age_cathegory }')      
 
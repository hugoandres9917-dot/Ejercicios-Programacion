employee_info  = {
    'name': 'Hugo',
    'email':'hugo.andres99@hotmail.com',
    'grade': 3,
    'age': 37
}
key_eliminartor = ['email','grade']

for item in key_eliminartor:
     employee_info.pop(item)
    
print(employee_info)
print(f'deletec intem {key_eliminartor}')
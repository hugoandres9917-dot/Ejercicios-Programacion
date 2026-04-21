employee_info  = {
    'name': 'Hugo',
    'email':'hugo.andres99@hotmail.com',
    'grade': 3,
    'age': 37
}
key_to_delete= ['email','grade']

for item in key_to_delete:
    employee_info.pop(item)
    
print(employee_info)
print(f'deletec intem {key_to_delete}')


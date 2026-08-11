#Cree una clase abstracta User con los siguientes métodos abstractos:
        #get_role()
        #has_permission(permission)
    #Luego cree dos clases que hereden de ella:
        #AdminUser
        #RegularUser
    #Cada una debe implementar los métodos
        #Por ejemplo:
            #AdminUser siempre tiene permisos
            #RegularUser solo tiene permisos limitados ("read", por ejemplo)
            
            
from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def has_permission(self, permission):
        pass
    
class AdminUser(User):
    def __init__(self, name):
        self.name = name
        
    def get_role(self):
        return "Administrador" # AdminUser tiene el rol de "Administrador"
    
    def has_permission(self, permission):
        return True  # AdminUser siempre tiene permisos
    
class RegularUser(User):
    def __init__(self, name):
        self.name = name
        
    def get_role(self):
        return "Usuario Regular" # RegularUser tiene el rol de "Usuario Regular"
    
    def has_permission(self, permission):
        return permission == "read"  # RegularUser solo tiene permisos limitados ("read")
    
# Ejemplo de uso
try:
    user1= AdminUser("Hugo")
    user2 = RegularUser("Andrea")
    
    print(user1.get_role()) # Imprime el rol del usuario 1
    print(user2.get_role()) # Imprime el rol del usuario 2  
    print(user1.has_permission("delete")) # AdminUser siempre tiene permisos, por lo que devuelve True
    print(user2.has_permission("delete")) # RegularUser solo tiene permisos limitados, por lo que devuelve False
except Exception as e:
    print(e)
    
    
    
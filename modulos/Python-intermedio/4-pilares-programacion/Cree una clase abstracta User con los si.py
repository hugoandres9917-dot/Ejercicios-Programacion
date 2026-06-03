

class User:
    def get_role(self):
        raise NotImplementedError("Subclasses must implement this method")

    def has_permission(self, permission):
        raise NotImplementedError("Subclasses must implement this method")              
    
class AdminUser(User):
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True  # Admin users have all permissions

class RegularUser(User):
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Regular"

    def has_permission(self, permission):
        return permission == "read"  # Regular users only have "read" permission
    

# Ejemplo de uso
user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")       
print(user1.has_permission("delete"))  # True
print(user2.has_permission("delete"))  # False


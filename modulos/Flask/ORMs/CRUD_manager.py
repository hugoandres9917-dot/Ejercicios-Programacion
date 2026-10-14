#Manager Logica CRUD

from typing import List, Optional
from sqlalchemy import  select
from database import SessionLocal
from ORMs_Models import User, Address, Vehicle
from sqlalchemy.exc import IntegrityError

class UserManager:
    @staticmethod
    def create_user(name: str, email: str) -> Optional[User]:
        with SessionLocal() as session:
            try:     
                user = User(name=name, email=email)
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
            except IntegrityError:
                session.rollback()
                raise ValueError(f"El usuario con email '{email}' ya existe.")
    
    @staticmethod
    def update_user(user_id: int, name: Optional[str]= None, email: Optional[str] = None) -> Optional[User]:
        with SessionLocal() as session:
            user = session.get(User, user_id)
            if user:
                if name: user.name = name
                if email: user.email = email
                session.commit()
                session.refresh(user)
            return user
    
    @staticmethod
    def delete_user(user_id: int) -> bool:
        with SessionLocal() as session:
            user = session.get(User, user_id)
            if user:
                session.delete(user)
                session.commit()
                return True
            return False
        
    @staticmethod
    def get_all_users() -> List[User]:
        with SessionLocal() as session:
            return list(session.scalars(select(User)).all())
        

class VehicleManager:
    @staticmethod
    def create_vehicle(brand: str, model: str, user_id: Optional[int] = None) -> Vehicle:
        with SessionLocal() as  session:
            vehicle = Vehicle(brand=brand, model=model, user_id=user_id)
            session.add(vehicle)
            session.commit()
            session.refresh(vehicle)
            return vehicle
        
    @staticmethod
    def update_vehicle(vehicle_id: int, brand: Optional[str] = None, model: Optional[str] = None) -> Optional[Vehicle]:
        with SessionLocal() as session:
            vehicle = session.get(Vehicle, vehicle_id)
            if vehicle:
                if brand: vehicle.brand = brand
                if model: vehicle.model = model
                session.commit()
                session.refresh(vehicle)
            return vehicle
        
    @staticmethod
    def delete_vehicle(vehicle_id: int) -> bool:
        with SessionLocal() as session:
            vehicle = session.get(Vehicle, vehicle_id)
            if vehicle:
                session.delete(vehicle)
                session.commit()
                return True
            return False
        
    @staticmethod
    def assign_vehicle_to_user(vehicle_id: int, user_id: int) -> Optional[Vehicle]:
        with SessionLocal() as  session:
            vehicle = session.get(Vehicle, vehicle_id)# asociar un automovil a un usuario
            user = session.get(User, user_id)
            if vehicle and user:
                vehicle.user_id = user.id
                session.commit()
                session.refresh(vehicle)
                return vehicle
            return None
        
    @staticmethod
    def get_all_vehicles() -> List[Vehicle]:
        with SessionLocal() as  session:
            return list(session.scalars(select(Vehicle)).all())
        
        
class AddressManager:
    @staticmethod
    def create_address(street: str, city: str, user_id: int) -> Address:  
        with SessionLocal() as session:
            user = session.get(User, user_id) #validacion de usuario existente antes de crear la direccion
            if not user:
                print(f"Error: No se puede crear la dirección porque el usuario con ID {user_id} no existe.")
                return None
            address = Address(street=street, city=city, user_id=user_id)
            session.add(address)
            session.commit()
            session.refresh(address)
            return address
        
    @staticmethod
    def update_address(address_id: int, street: Optional[str] = None, city: Optional[str] = None) -> Optional[Address]:
        with SessionLocal() as session:
            address = session.get(Address, address_id)
            if address:
                if street: address.street = street
                if city: address.city = city
                session.commit()
                session.refresh(address)
                return address
            
    @staticmethod
    def delete_address(address_id: int) -> bool:
        with SessionLocal() as session:
            address = session.get(Address, address_id)
            if address:
                session.delete(address)
                session.commit()
                return True
            return False
        
    @staticmethod
    def get_all_addresses() -> List[Address]:
            with SessionLocal() as session:
                return list(session.scalars(select(Address)).all())
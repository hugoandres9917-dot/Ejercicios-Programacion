#Manager Logica CRUD.

from typing import List, Optional
from sqlalchemy import func, select
from sqlalchemy.orm import selectinload
from database import SessionLocal
from ORMs_Models import User, Address, Vehicle

class UserManager:
    @staticmethod
    def create_user(name: str, email: str) -> User:
        with SessionLocal() as session:
            user = User(name=name, email=email)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
    
    @staticmethod
    def update_user(user_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Optional[User]:
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
    
    # Ejercicio extra 1.2: Usuarios con más de 1 auto
    @staticmethod
    def get_users_with_multiple_vehicles() -> List[User]:
        with SessionLocal() as session:
            stmt = select(User).options(selectinload(User.autos))
            users = session.scalars(stmt).all()
            # Filtramos en Python o directamente en SQL aquellos con len(autos) > 1
            return [u for u in users if len(u.autos) > 1]
    
    # Ejercicio extra 2: punto 2
    # Imprimir autos y direcciones usando usuario.autos y usuario.direcciones
    @staticmethod
    def get_user_with_vehicles_and_addresses(user_id: int) -> None:
        with SessionLocal() as session:
            stmt = (
                select(User)
                .options(
                    selectinload(User.autos),
                    selectinload(User.direcciones)
                )
                .where(User.id == user_id)
            )
            # Ejecución correcta del statement precargado
            user = session.scalars(stmt).first()

            if not user:
                print(f"No se encontró el usuario con ID {user_id}")
                return

            print(f"\n=== Detalles del Usuario: {user.name} (ID: {user.id}) ===")
            
            print("\n--- Automóviles Asociados ---")
            if user.autos:
                for auto in user.autos:
                    print(f"ID: {auto.id}, Marca: {auto.brand}, Modelo: {auto.model}")
            else:
                print("No hay automóviles asociados.")

            print("\n--- Direcciones Asociadas ---")
            if user.direcciones:
                for address in user.direcciones:
                    print(f"ID: {address.id}, Calle: {address.street}, Ciudad: {address.city}")
            else:
                print("No hay direcciones asociadas.")
                

class VehicleManager:
    @staticmethod
    def create_vehicle(brand: str, model: str, user_id: Optional[int] = None) -> Vehicle:
        with SessionLocal() as session:
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
        with SessionLocal() as session:
            vehicle = session.get(Vehicle, vehicle_id)
            user = session.get(User, user_id)
            if vehicle and user:
                vehicle.user_id = user.id
                session.commit()
                session.refresh(vehicle)
                return vehicle
            return None
        
    @staticmethod
    def get_all_vehicles() -> List[Vehicle]:
        with SessionLocal() as session:
            return list(session.scalars(select(Vehicle)).all())
        
    # Ejercicio extra 1.1: Automóviles sin usuario asignado
    @staticmethod
    def get_vehicles_without_user() -> List[Vehicle]:
        with SessionLocal() as session:
            stmt = select(Vehicle).where(Vehicle.user_id.is_(None))
            return list(session.scalars(stmt).all())


class AddressManager:
    @staticmethod
    def create_address(street: str, city: str, user_id: int) -> Address:  
        with SessionLocal() as session:
            user = session.get(User, user_id)
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

    # Ejercicion extra  1.3: Direcciones por coincidencias en el nombre de calle
    @staticmethod
    def get_addresses_by_street(street_name: str) -> List[Address]:
        with SessionLocal() as session:
            stmt = select(Address).where(Address.street.ilike(f"%{street_name}%"))
            return list(session.scalars(stmt).all())
        
    @staticmethod
    def get_addresses_by_street_substring(substring: str) -> List[Address]:
        with SessionLocal() as session:
            # Filtra las direcciones cuyo campo street contenga el substring indicado
            stmt = select(Address).where(Address.street.ilike(f"%{substring}%"))
            return list(session.scalars(stmt).all())
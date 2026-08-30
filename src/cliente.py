from abc import ABC, abstractmethod

from .producto import Producto


class Cliente(ABC):
    def __init__(self, nombre: str, email: str, ciudad: str):
        self.nombre = nombre
        self.email = email
        self.ciudad = ciudad

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self._nombre = valor

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El email no puede estar vacío.")

        self._email = valor

    @property
    def ciudad(self) -> str:
        return self._ciudad

    @ciudad.setter
    def ciudad(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La ciudad no puede estar vacía.")

        self._ciudad = valor

    def comprar(self, producto: Producto) -> None:
        if producto is None:
            raise ValueError("El producto no puede ser nulo.")

        if producto.hay_stock():
            producto.stock -= 1
            print(f"{self.nombre} compró {producto.nombre}")
        else:
            print(f"No hay stock disponible de {producto.nombre}")

    @abstractmethod
    def calcular_descuento(self) -> float:
        pass

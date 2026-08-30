from .cliente import Cliente


class ClienteMayorista(Cliente):
    def calcular_descuento(self) -> float:
        return 0.20

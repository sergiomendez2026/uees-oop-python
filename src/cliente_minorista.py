from .cliente import Cliente


class ClienteMinorista(Cliente):
    def calcular_descuento(self) -> float:
        return 0.05

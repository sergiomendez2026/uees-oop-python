from .cliente import Cliente
from .item_proforma import ItemProforma


class Proforma:

    def __init__(self, cliente: Cliente) -> None:
        if cliente is None:
            raise ValueError(
                "El cliente no puede ser nulo."
            )

        self._cliente = cliente
        self._items: list[ItemProforma] = []

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def items(self) -> list[ItemProforma]:
        return self._items.copy()

    def agregar_item(self, item: ItemProforma) -> None:
        if item is None:
            raise ValueError(
                "El item no puede ser nulo."
            )

        self._items.append(item)

    def calcular_total(self) -> float:
        total = 0.0

        for item in self._items:
            total += item.calcular_subtotal()

        return total
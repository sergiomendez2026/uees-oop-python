from .producto import Producto


class ItemProforma:

    def __init__(
        self,
        producto: Producto,
        cantidad: int
    ) -> None:
        if producto is None:
            raise ValueError("El producto no puede ser nulo.")

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        self._producto = producto
        self._cantidad = cantidad

    @property
    def producto(self) -> Producto:
        return self._producto

    @property
    def cantidad(self) -> int:
        return self._cantidad

    def calcular_subtotal(self) -> float:
        return self._producto.precio * self._cantidad
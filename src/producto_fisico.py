from .producto import Producto


class ProductoFisico(Producto):

    def __init__(
        self,
        nombre: str,
        precio: float,
        stock: int,
        peso: float,
        ubicacion_almacen: str
    ) -> None:
        super().__init__(nombre, precio, stock)
        self.peso = peso
        self.ubicacion_almacen = ubicacion_almacen

    @property
    def peso(self) -> float:
        return self._peso

    @peso.setter
    def peso(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El peso no puede ser negativo.")

        self._peso = valor

    @property
    def ubicacion_almacen(self) -> str:
        return self._ubicacion_almacen

    @ubicacion_almacen.setter
    def ubicacion_almacen(self, valor: str) -> None:
        if valor is None or not valor.strip():
            raise ValueError(
                "La ubicación del almacén no puede estar vacía."
            )

        self._ubicacion_almacen = valor
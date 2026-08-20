from .producto import Producto


class ProductoDigital(Producto):

    def __init__(
        self,
        nombre: str,
        precio: float,
        stock: int,
        tamano_mb: float,
        url_descarga: str
    ) -> None:
        super().__init__(nombre, precio, stock)
        self.tamano_mb = tamano_mb
        self.url_descarga = url_descarga

    @property
    def tamano_mb(self) -> float:
        return self._tamano_mb

    @tamano_mb.setter
    def tamano_mb(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El tamaño no puede ser negativo.")

        self._tamano_mb = valor

    @property
    def url_descarga(self) -> str:
        return self._url_descarga

    @url_descarga.setter
    def url_descarga(self, valor: str) -> None:
        if valor is None or not valor.strip():
            raise ValueError(
                "La URL de descarga no puede estar vacía."
            )

        self._url_descarga = valor
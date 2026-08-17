from .cliente import Cliente
from .producto import Producto


def main() -> None:
    producto = Producto(
        "Laptop",
        850.00,
        2
    )

    cliente = Cliente(
        "Sergio",
        "sergio@email.com",
        "Guayaquil"
    )

    print(f"Stock inicial: {producto.stock}")

    cliente.comprar(producto)

    print(f"Stock final: {producto.stock}")


if __name__ == "__main__":
    main()
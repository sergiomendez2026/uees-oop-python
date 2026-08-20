from .cliente import Cliente
from .item_proforma import ItemProforma
from .producto_digital import ProductoDigital
from .producto_fisico import ProductoFisico
from .proforma import Proforma


def main() -> None:
    cliente = Cliente(
        "Sergio",
        "sergio@email.com",
        "Guayaquil"
    )

    laptop = ProductoFisico(
        "Laptop",
        850.00,
        2,
        2.1,
        "Bodega A"
    )

    curso = ProductoDigital(
        "Curso Python",
        120.00,
        100,
        1500.0,
        "https://ejemplo.com/curso"
    )

    item_laptop = ItemProforma(
        laptop,
        1
    )

    item_curso = ItemProforma(
        curso,
        2
    )

    proforma = Proforma(cliente)

    proforma.agregar_item(item_laptop)
    proforma.agregar_item(item_curso)

    print("Producto fisico:", laptop.nombre)
    print("Peso:", laptop.peso, "kg")
    print("Ubicacion:", laptop.ubicacion_almacen)

    print()

    print("Producto digital:", curso.nombre)
    print("Tamano:", curso.tamano_mb, "MB")
    print("URL:", curso.url_descarga)

    print()

    print(
        "Subtotal Laptop: $",
        item_laptop.calcular_subtotal(),
        sep=""
    )

    print(
        "Subtotal Curso: $",
        item_curso.calcular_subtotal(),
        sep=""
    )

    print(
        "Total Proforma: $",
        proforma.calcular_total(),
        sep=""
    )


if __name__ == "__main__":
    main()
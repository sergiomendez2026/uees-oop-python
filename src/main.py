from .cliente_mayorista import ClienteMayorista
from .cliente_minorista import ClienteMinorista
from .item_proforma import ItemProforma
from .producto_digital import ProductoDigital
from .producto_fisico import ProductoFisico
from .proforma import Proforma


def main() -> None:
    cliente_mayorista = ClienteMayorista(
        "Sergio",
        "sergio@email.com",
        "Guayaquil"
    )

    cliente_minorista = ClienteMinorista(
        "Ana",
        "ana@email.com",
        "Quito"
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

    item_laptop_mayorista = ItemProforma(
        laptop,
        1
    )

    item_curso_mayorista = ItemProforma(
        curso,
        2
    )

    item_laptop_minorista = ItemProforma(
        laptop,
        1
    )

    item_curso_minorista = ItemProforma(
        curso,
        2
    )

    proforma_mayorista = Proforma(cliente_mayorista)

    proforma_mayorista.agregar_item(
        item_laptop_mayorista
    )

    proforma_mayorista.agregar_item(
        item_curso_mayorista
    )

    proforma_minorista = Proforma(cliente_minorista)

    proforma_minorista.agregar_item(
        item_laptop_minorista
    )

    proforma_minorista.agregar_item(
        item_curso_minorista
    )

    print("Producto fisico:", laptop.nombre)
    print("Peso:", laptop.peso, "kg")
    print(
        "Ubicacion:",
        laptop.ubicacion_almacen
    )

    print()

    print(
        "Producto digital:",
        curso.nombre
    )

    print(
        "Tamano:",
        curso.tamano_mb,
        "MB"
    )

    print(
        "URL:",
        curso.url_descarga
    )

    print()

    print("=== PROFORMA CLIENTE MAYORISTA ===")
    print(
        "Cliente:",
        cliente_mayorista.nombre
    )

    print(
        "Descuento:",
        cliente_mayorista.calcular_descuento() * 100,
        "%"
    )

    print(
        "Subtotal Laptop: $",
        item_laptop_mayorista.calcular_subtotal(),
        sep=""
    )

    print(
        "Subtotal Curso: $",
        item_curso_mayorista.calcular_subtotal(),
        sep=""
    )

    print(
        "Total Proforma: $",
        proforma_mayorista.calcular_total(),
        sep=""
    )

    print()

    print("=== PROFORMA CLIENTE MINORISTA ===")
    print(
        "Cliente:",
        cliente_minorista.nombre
    )

    print(
        "Descuento:",
        cliente_minorista.calcular_descuento() * 100,
        "%"
    )

    print(
        "Subtotal Laptop: $",
        item_laptop_minorista.calcular_subtotal(),
        sep=""
    )

    print(
        "Subtotal Curso: $",
        item_curso_minorista.calcular_subtotal(),
        sep=""
    )

    print(
        "Total Proforma: $",
        proforma_minorista.calcular_total(),
        sep=""
    )


if __name__ == "__main__":
    main()

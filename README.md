# UEES - Programación Orientada a Objetos - Python

Proyecto académico desarrollado en Python para aplicar los conceptos fundamentales de programación orientada a objetos.

## Contenido

- Clases y objetos
- Encapsulación
- Properties y setters
- Asociación entre objetos
- Validación de atributos
- Diagrama UML

## Clases

### Producto

Atributos:

- nombre
- precio
- stock

Comportamiento:

- validación de nombre
- validación de precio
- validación de stock
- verificación de disponibilidad mediante `hay_stock()`

### Cliente

Atributos:

- nombre
- email
- ciudad

Comportamiento:

- validación de atributos
- compra de productos mediante `comprar()`

## Asociación

La clase `Cliente` utiliza objetos de la clase `Producto` mediante el método:

```python
cliente.comprar(producto)
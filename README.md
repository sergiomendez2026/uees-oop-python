# UEES - Programación Orientada a Objetos - Python

Proyecto desarrollado como parte de la asignatura de Programación Orientada a Objetos.

El sistema modela una empresa proveedora de tecnología y capacitación que puede atender tanto a personas naturales bajo un modelo B2C como a empresas bajo un modelo B2B.

## Objetivo

Aplicar los fundamentos de Programación Orientada a Objetos mediante el modelado de clientes, productos y proformas utilizando encapsulación, herencia, asociación y composición.

## Semana 1

Durante la Semana 1 se implementaron las clases:

- `Producto`
- `Cliente`

### Conceptos aplicados

- Clases y objetos
- Encapsulación
- Atributos privados
- Getters y setters
- Propiedades
- Asociación entre objetos

La clase `Producto` representa los artículos o servicios comercializados por la empresa.

La clase `Cliente` representa al comprador, que puede ser una persona natural o una empresa.

## Semana 2

Durante la Semana 2 se amplió el modelo incorporando herencia y composición.

### Herencia

La clase `Producto` funciona como clase base para:

- `ProductoFisico`
- `ProductoDigital`

`ProductoFisico` incorpora atributos específicos como:

- peso
- ubicación de almacenamiento

`ProductoDigital` incorpora atributos como:

- tamaño en MB
- URL de descarga

### Composición

La clase `Proforma` contiene una colección de objetos `ItemProforma`.

Cada `ItemProforma` relaciona:

- un producto
- una cantidad
- el cálculo del subtotal

La clase `Proforma` permite agregar diferentes ítems y calcular el total de la operación comercial.

## Clases principales

- `Cliente`
- `Producto`
- `ProductoFisico`
- `ProductoDigital`
- `ItemProforma`
- `Proforma`

## Modelo general

```text
Cliente
   |
   v
Proforma
   |
   v
ItemProforma
   |
   v
Producto
   ^
   |
   +-- ProductoFisico
   |
   +-- ProductoDigital

# Especificación de Requisitos de Software (SRS) - v1.0

## 1. Introducción
Este documento describe los requisitos para la primera versión de "StockLight".

## 2. Requisitos Funcionales (RF)
- **RF-001 (Alta de Producto):** El sistema debe permitir al usuario agregar un nuevo producto indicando nombre, precio y cantidad inicial.
- **RF-002 (Listado de Stock):** El sistema debe mostrar una lista de todos los productos registrados con su stock actual.
- **RF-003 (Actualizar Stock):** El sistema debe permitir modificar la cantidad de un producto existente (sumar o restar unidades).
- **RF-004 (Persistencia de Datos):** El sistema debe guardar automáticamente los cambios en un archivo local al cerrar la aplicación.

## 3. Requisitos No Funcionales (RNF)
- **RNF-001 (Portabilidad):** El sistema debe ser compatible con Windows, Linux y macOS.
- **RNF-002 (Tiempo de Respuesta):** Las consultas de inventario deben mostrar resultados en menos de 2 segundos para bases de datos de hasta 1000 productos.
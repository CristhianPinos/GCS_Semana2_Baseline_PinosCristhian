# Documento de Diseño de Software (SDD) - v1.0

## 1. Arquitectura del Sistema
StockLight sigue una arquitectura MVC adaptada a consola:
- **Modelo:** Gestión de datos y lógica de negocio (inventario).
- **Vista:** Interfaz de línea de comandos (CLI) para interactuar con el usuario.
- **Controlador:** Orquestador que recibe inputs y llama al modelo.

## 2. Componentes Principales
- **InventoryManager (Class):** Responsable de leer/escribir en el archivo JSON y mantener la lista de objetos en memoria.
- **CLIInterface (Class):** Responsable de los `print` y `input` del usuario.
- **Product (Class):** Entidad que representa un artículo (ID, nombre, precio, cantidad).

## 3. Decisiones Técnicas
- **Almacenamiento:** Se utilizará formato JSON por ser ligero y nativo en Python.
- **Interfaz:** CLI estándar para evitar dependencias gráficas pesadas.
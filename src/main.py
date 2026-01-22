import sys

class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, name):
        self.products.append(name)
        return True

def main():
    manager = InventoryManager()
    print("---- StockLight v1.0 Release ----")
    print("Sistema listo para operar.")
    manager.add_product("Manzanas")
    print(f"Inventario cargado: {len(manager.products)} productos.")

if __name__ == "__main__":
    main()
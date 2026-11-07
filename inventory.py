class InventoryManager:
    def __init__(self):
        # Stores items as {name: {"quantity": int, "price": float}}
        self.inventory = {}

    def add_item(self, name, quantity, price):
        if name in self.inventory:
            self.inventory[name]["quantity"] += quantity
            self.inventory[name]["price"] = price 
        else:
            self.inventory[name] = {"quantity": quantity, "price": price}

    def remove_item(self, name):
        if name in self.inventory:
            del self.inventory[name]
        else:
            print(f"Error: {name} not found in inventory.")

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        for name, details in self.inventory.items():
            print(f"{name}: {details['quantity']} pcs, ${details['price']} each")

if __name__ == "__main__":
    # Simple Testing
    manager = InventoryManager()
    manager.add_item("Laptop", 5, 999.99)
    manager.add_item("Wireless Mouse", 15, 25.50)
    manager.view_inventory()
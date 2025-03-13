from pydantic import BaseModel
from typing import Dict
from product import Product

class InventoryManagement(BaseModel):
    products: Dict[Product, int] # dictionary of products and quantity

    def add_product(self, product: Product) -> None:
        """Adds a product to inventory. If it exists, updates quantity."""
        try:
            self.products[product] = self.products.get(product, 0) + 1
        except Exception as e:
            raise ValueError(f"Failed to add product: {e}")

    def get_product(self, product_name: str) -> Product:
        """Retrieves a product by name."""
        try:
            return next(product for product in self.products if product.name.lower() == product_name.lower())
        except StopIteration:
            raise ValueError(f"No such product exists: {product_name}")

    def reduce_quantity(self, product_name: str) -> None:
        """Reduces product quantity. Removes the product if quantity reaches zero."""
        try:
            product = self.get_product(product_name)
            if self.products[product] > 1:
                self.products[product] -= 1
            else:
                self.remove_product(product)
        except ValueError as e:
            raise ValueError(f"Cannot reduce quantity: {e}")

    def remove_product(self, product: Product) -> None:
        """Removes a product completely from inventory."""
        try:
            del self.products[product]
        except KeyError:
            raise ValueError(f"Cannot remove: Product '{product.name}' does not exist in inventory.")

    def total_inventory_value(self) -> float:
        """Calculates total value of all products in inventory."""
        return sum(product.price * quantity for product, quantity in self.products.items())




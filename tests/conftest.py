import pytest
from ..inventory.product import Product
from ..inventory.inventory_management import InventoryManagement

@pytest.fixture
def product1():
    return Product(name="Laptop", price=1000.0, description="Gaming laptop", id=1)

@pytest.fixture
def inventory():
    return InventoryManagement(products={})

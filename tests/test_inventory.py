import pytest

def test_add_product(inventory, product1):
    """Test adding a product to the inventory."""
    inventory.add_product(product1)
    # After adding, check if the product exists with quantity 1
    assert product1 in inventory.products  # Check if the product object is a key in the dictionary
    assert inventory.products[product1] == 1  # Check if the quantity is 1


def test_reduce_quantity(inventory, product1):
    """Test reducing the quantity of a product."""
    inventory.add_product(product1)
    inventory.reduce_quantity("Laptop")
    # After reducing, the quantity of 'Laptop' should be 0, and it should be removed
    assert product1.id not in inventory.products  # Product should be removed after quantity reaches 0

    # Trying to reduce again should raise a ValueError
    with pytest.raises(ValueError, match="Cannot reduce quantity: No such product exists: Laptop"):
        inventory.reduce_quantity("Laptop")


def test_remove_product(inventory, product1):
    """Test removing a product from the inventory."""
    inventory.add_product(product1)
    inventory.remove_product(product1)
    # Check that the product is removed from the inventory
    assert product1.id not in inventory.products


def test_total_inventory_value(inventory, product1):
    """Test total inventory value calculation."""
    inventory.add_product(product1)
    assert inventory.total_inventory_value() == 1000.0  # 1 * 1000 (product price)


def test_get_product(inventory, product1):
    """Test retrieving a product by name."""
    inventory.add_product(product1)
    retrieved_product = inventory.get_product("Laptop")
    assert retrieved_product == product1

from inventory.product import Product

def test_product_creation(product1):
    """Test the creation of a Product."""
    assert product1.name == "Laptop"
    assert product1.price == 1000.0
    assert product1.description == "Gaming laptop"
    assert product1.id == 1
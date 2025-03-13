This is an Inventory Management System implemented in Python using the pydantic library.
It allows you to manage products in an inventory, where you can add products, reduce their quantities, and remove them when necessary.
The system supports basic inventory operations such as adding, removing, and updating quantities of products. 

Features:
- Product Management: Add, remove, and update product quantities.
- Inventory Management: Track product quantities and total value of the inventory.
- Error Handling: Includes checks for product existence and handles edge cases (e.g., trying to reduce the quantity of a non-existent product).

Structure:
- Product Class: Defines a product with attributes like name, price, description, and id.
- InventoryManagement Class: Handles the operations related to inventory, including adding and removing products, reducing quantities, and calculating the total value of the inventory.

Test Scenarios:
- Add Product: Test adding a product and ensuring its presence in the inventory with the correct quantity.
- Reduce Quantity: Test reducing the quantity of a product and checking if the quantity is updated correctly.
- Remove Product: Test removing a product from the inventory and verifying that it no longer exists.

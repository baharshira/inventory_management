from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    description: str
    id: int

    # Implementing __hash__ and __eq__ to make Product hashable
    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: any) -> bool:
        if not isinstance(other, Product):
            return False
        return self.id == other.id  # Compare products by their ID


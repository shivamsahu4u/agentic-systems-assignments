from pydantic import BaseModel, Field, EmailStr, constr, ValidationError
from typing import Optional

# Address Model
class Address(BaseModel):
    city: str = Field(..., min_length=3, description="City name must be at least 3 characters")
    pincode: str = Field(..., pattern=r'^\d{6}$')  # exactly 6 digits

# User Model
class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(..., ge=18, description="Age must be 18 or older")
    address: Address
    is_premium: Optional[bool] = False

# Example usage
try:
    user = User(
        user_id=1,
        name="Shivam",
        email="shivam@example.com",
        age=22,
        address={"city": "Bengaluru", "pincode": "560001"}
    )
    print("✅ Valid user:", user.dict())
except ValidationError as e:
    print("❌ Validation failed:\n", e)

# Invalid example
try:
    user = User(
        user_id=2,
        name="Sam",
        email="invalid-email",
        age=15,
        address={"city": "NY", "pincode": "123"}
    )
    print("✅ Valid user:", user.dict())
except ValidationError as e:
    print("❌ Validation failed:\n", e)
from pydantic import BaseModel, Field, EmailStr, ValidationError

class UserRegister(BaseModel):
    username: str = Field(..., min_length=5, description="Username must be at least 5 characters")
    email: EmailStr
    age: int = Field(..., ge=18, description="Age must be 18 or older")

# Example usage
try:
    user = UserRegister(username="Shivam", email="shivam@abc.com", age=28)
    print("✅ Valid user:", user)
except ValidationError as e:
    print("❌ Validation failed:\n", e)

# Invalid example
try:
    user = UserRegister(username="Sam", email="invalid-email", age=15)
    print("✅ Valid user:", user)
except ValidationError as e:
    print("❌ Validation failed:\n", e)
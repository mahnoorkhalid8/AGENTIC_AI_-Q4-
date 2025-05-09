from pydantic import BaseModel, EmailStr, validator, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: List[Address]
    
    @validator("name")
    def validate_name(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

# Invalid data
try:
    invalid_user = UserWithAddress(
        id=2,
        name="M",                   # too short(invalid)
        email="mahnoor@gmail.com",
        address=[Address(street="17 Est street", city="Karachi", zip_code="12345")],
    )
except ValidationError as e:
    print("Validation Error:", e)
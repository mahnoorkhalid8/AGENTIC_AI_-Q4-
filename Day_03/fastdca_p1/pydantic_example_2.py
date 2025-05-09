from pydantic import BaseModel, EmailStr

# Define a nested model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: list[Address]
    
# Valid data with nested model
user_data = {
    "id": 1,
    "name": "Mahnoor",
    "email": "mahnoorkhalid@gmail.com",
    "address": [
        {"street": "17 Est street", "city": "Karachi", "zip_code": "12345"},
        {"street": "123 street", "city": "Islamabad", "zip_code": "54321"}
    ],
}

user = UserWithAddress.model_validate(user_data)
print(user.model_dump())
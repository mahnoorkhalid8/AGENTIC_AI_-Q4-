from pydantic import BaseModel, ValidationError

# Define a Pydantic model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None
    
# Valid data
user_data = {"id": 1, "name": "Mahnoor", "email": "mahnoorkhalid814@gmail.com", "age": 23}
user = User(**user_data)         # type: ignore
print(user)
print(user.model_dump())

# Invalid data
try:
    invalid_user = User(id="hello", name="Khalid", email="khalid@gmail.com")        # type: ignore
except ValidationError as e:
    print("Validation Error:", e)

    
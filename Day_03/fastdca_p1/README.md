# What is Pydantic?
Pydantic is a data validation and settings management library for Python, based on Python type annotations.

# 🚀 Features:

1. Strong data validation using Python type hints
2. Automatic parsing and error handling
3. Support for nested data models
4. Custom field-level validation
5. Clean serialization to dict and JSON

# Concepts Covered
🔹 Basic Pydantic Model:
Create structured models using BaseModel with type hints. Automatically validates data at runtime.

🔹 Field Customization:
Customize fields using Field() to add constraints like minimum/maximum values, lengths, and defaults.

🔹 Nested Models:
Models can contain other models — ideal for structured or hierarchical data like user profiles and addresses.

🔹 Custom Validators:
Add custom rules using @validator decorators to ensure complex conditions on input fields.

🔹 Error Handling:
Built-in ValidationError for catching and displaying informative messages if input data is incorrect.

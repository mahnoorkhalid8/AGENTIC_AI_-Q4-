# 🚀 FastAPI Project – Hello World by Mahnoor Khalid
This is a simple FastAPI project that returns a greeting message using a GET endpoint. The project uses a virtual environment and follows modern FastAPI setup standards using uv.

# 📁 Project Setup Steps
# 1. 📦 Create and Initialize the Project Folder

uv init fast_api

This will create a project folder with FastAPI standard layout.
Set up a virtual environment.

# 2. ✅ Install FastAPI and Required Tools

uv pip install fastapi[standard]

This installs:
fastapi
uvicorn (ASGI server)
and other standard FastAPI dependencies.

# 3. 🧪 Verify Virtual Environment Activation (if needed)

Windows:
.venv\Scripts\activate

Mac/Linux:
source .venv/bin/activate

# 4. 📝 Create the FastAPI App in main.py

Write your code here

# 5. 🚦 Run the FastAPI App

In the terminal, run the app using:

uvicorn main:app --reload

main: Your file name without .py
app: Your FastAPI app object
--reload: Auto-reloads on code changes

# 6. 🌐 Open Your App in the Browser

Once the server is running, visit:

Main route: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs

You will see the response and can test it via Swagger UI as well.

# 🛠 Tools Used

FastAPI – Web framework for building APIs.
uvicorn – ASGI server for serving FastAPI.
uv – Modern Python packaging tool.
Swagger UI – For auto-generated API documentation.

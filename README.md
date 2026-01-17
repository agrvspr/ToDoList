# Warframe Farming List Tracker
A simple web application to track items you need to farm in Warframe. Built with FastAPI and SQLite.
Features

## Project Structure
ToDoList/
- main.py                          # FastAPI application entry point
- index.html                       # Web interface
- schema.sql                       # Database schema
- tasks.db                         # SQLite database (created automatically)
- models/
- task.py                      # Pydantic models
- services/
- task_manager.py              # Logic layer
- repositories/
- task_repository.py           # Database operations

Requirements

Python 3.7+, 
FastAPI, 
Uvicorn, 
Pydantic, 
SQLite3 (included with Python)


### Running the Application

Start the server:

bash   python -m uvicorn main:app --reload

Open your browser and go to:
   http://127.0.0.1:8000

Start tracking your Warframe farming items!

Usage
Adding Items

Type the item name in the input field (e.g., "Khora Prime", "Kuva Bramma", "Argon Crystals")
Click "Add Item"
The item appears in your list below

Deleting Items

Click the "Delete" button next to any item to remove it from your list

Data Persistence

All items are saved in tasks.db
Your list will still be there when you restart the application
To reset everything, just delete the tasks.db file

API Endpoints
The application provides a REST API:

GET / - Serves the web interface
GET /tasks - Get all farming items
POST /tasks - Add a new item

Body: {"title": "item name"}


DELETE /tasks/{id} - Delete an item by ID

API Documentation
FastAPI automatically generates interactive API documentation:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc


Technologies Used

FastAPI - Modern Python web framework
SQLite - Lightweight database
HTML/CSS/JavaScript - Frontend interface
Uvicorn - ASGI server

from fastapi import FastAPI, HTTPException
from services.task_manager import TaskManager
from repositories.task_repository import TaskRepository
from models.task import TaskCreate

repo = TaskRepository()
manager = TaskManager(repo)

app = FastAPI(title= "Todo API")

#Since I am on windows run with (python -m uvicorn main:app --reload)
#will show up on http://127.0.0.1:8000/docs 


#Create task
@app.post("/tasks")
def create_task(task: TaskCreate):
    task_id = manager.add_task(task.title)
    return {"id": task_id, "title": task.title}

#Read the tasks
@app.get("/tasks")
def list_tasks():
    return [{"id": t[0], "title": t[1], "completed": t[2]} for t in manager.list_tasks()]

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        manager.delete_task(task_id)
        return {"message": "Task deleted"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")


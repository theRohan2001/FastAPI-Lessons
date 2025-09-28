from fastapi import FastAPI, HTTPException, status
from .operations import read_all_tasks, read_task, create_task, modify_task, remove_task
from .models import TaskWithID, Task, UpdateTask

app = FastAPI()

@app.get("/tasks")
def read_tasks():
    tasks = read_all_tasks()
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskWithID)
def get_task(task_id: int):
    task = read_task(task_id)
    return task

@app.post("/task", response_model=TaskWithID)
def add_task(task: Task):
    return create_task(task)

@app.put("/tasks/{task_id}", response_model= UpdateTask)
def update_task(task_id: int, task: UpdateTask):
    upadated = modify_task(task_id, task.model_dump())
    if not upadated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    
    return upadated

@app.delete("/task/{task_id}")
def delete_task(task_id: int):
    deleted = remove_task(task_id)
    return  deleted


import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI()


class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: str
    completed: bool = False


tasks = {}


@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: UUID):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: Task):
    task.id = uuid4()
    tasks[task.id] = task
    return task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: UUID, task_update: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks[task_id]
    task.title = task_update.title
    task.description = task_update.description
    task.completed = task_update.completed
    tasks[task_id] = task
    return task


@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: UUID):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks.pop(task_id)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

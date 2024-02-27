from fastapi import FastAPI
from celery_worker import some_task, celery_app
from celery.result import AsyncResult
import asyncio

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/some_task")
async def do_some_task(delay: int):
    result = some_task.delay(delay)
    return {'task_id': result.id}

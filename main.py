from fastapi import FastAPI
from routers import game_data
import uvicorn

app = FastAPI()
app.include_router(game_data.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
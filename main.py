from fastapi import FastAPI
from routers import game_data
import uvicorn

app = FastAPI()
app.include_router(game_data.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=10000, log_level="info", reload=True)

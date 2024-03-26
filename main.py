import logging
from fastapi import FastAPI
import uvicorn

from load_env import env



PORT = int(env.get("PORT", 5000))
HOST_URI = env.get('HOST_URI', 'localhost')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()



# import routers
from game.route import game_router

routers = [game_router]

for router in routers: app.include_router(router)

if __name__ == "__main__":
    # run main server
    uvicorn.run("main:app", host=HOST_URI, port=PORT, log_level="info", reload=True)

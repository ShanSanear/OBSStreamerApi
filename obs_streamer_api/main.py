import uvicorn
from fastapi import FastAPI, APIRouter

from obs_streamer_api.routers import obs, storage, youtube

main_router = APIRouter(prefix='')


@main_router.get("/")
async def root():
    return {"messsage": "Hello world!"}


def create_app():
    app = FastAPI()
    app.include_router(main_router)
    app.include_router(obs.router)
    app.include_router(storage.router)
    app.include_router(youtube.router)
    return app


def main():
    app = create_app()
    uvicorn.run(app=app)


if __name__ == '__main__':
    main()

from fastapi import FastAPI
from server import routers
import uvicorn, settings
from fastapi.responses import RedirectResponse

app = FastAPI(title="Hospital")

[app.include_router(router) for router in routers]

@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app="start_server:app", host=settings.HOST, port=settings.PORT, reload=True)

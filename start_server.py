from fastapi import FastAPI
from server.router_list import router_list
import uvicorn
from settings import CREATE_PATH, FILL_PATH, PORT, HOST
from fastapi.responses import RedirectResponse
from server.database.db_manager import db_manager

app = FastAPI(title="Hospital")

[app.include_router(router) for router in router_list]


@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    if not db_manager.check_base():
        db_manager.execute_sql_script(CREATE_PATH, FILL_PATH)
    uvicorn.run(app="start_server:app", host=HOST, port=PORT, reload=True)

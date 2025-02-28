from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from superAdmin.controllers.login import router
from superAdmin.controllers.laptops import laptops
from superAdmin.controllers.desktop import desktop
from superAdmin.controllers.otherSystems import other_systems

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router,tags=["login"])
app.include_router(laptops,tags=["managing system data"])
app.include_router(desktop,tags=["desktop dashboard data"])
app.include_router(other_systems,tags=["other systems dashboard.."])


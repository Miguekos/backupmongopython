import uvicorn
from datetime import datetime, time, timedelta
from enum import Enum
from typing import List, Optional, Set
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, Field
from fastapi.responses import FileResponse
from backup import backup_db, listar_db
import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print("hostname:", hostname)
print("IP:", IP)

app = FastAPI()


class Listar(BaseModel):
    ip: str
    port: str = "27017"
    user: str = ""
    password: str = ""


class Backup(Listar):
    db: str = Field(None, description="Debes definir el nombre de la base de datos", min_length=1)


@app.get("/file/{name}")
async def main(name):
    try:
        return FileResponse("./tmp/{}".format(name))
    except:
        return {"message": "Su archivo {} ya no existe".format(name)}


@app.post("/backup")
async def backupmongo(backup: Backup):
    print(backup)
    back_up_dict = backup.dict()
    # print(back_up_dict["db"])
    backup_db(back_up_dict)
    return {
        "url": "http://{}:8000/file/{}.zip".format(IP, back_up_dict["db"])
    }


@app.post("/listarTablas")
async def backupmongo(listar: Listar):
    print(listar)
    db = listar_db(listar.dict())
    return db


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="info", reload=True, access_log=False)

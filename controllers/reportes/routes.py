from fastapi.responses import FileResponse
from .logic import ReporteProcess
from .models import Reportes
from datetime import datetime, time, timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException

reportes_router = APIRouter()

@reportes_router.get("/file/{folder}/{name}")
async def file(folder, name):
    try:
        return FileResponse("./tmp/{}/{}".format(folder, name))
    except:
        return {"message": "Su archivo {} ya no existe".format(name)}

@reportes_router.post("/")
async def reportes(item: Reportes, q: Optional[str] = None):
    reporte = ReporteProcess(item.dict())
    reporet = reporte.inicio()
    print("reporet", reporet)
    return {
        "xls" : "http://127.0.0.1:8000/api/v1/reportes/file/{}/{}.xls".format(reporet, reporet),
        "json" : "http://127.0.0.1:8000/api/v1/reportes/file/{}/{}.json".format(reporet, reporet),
        "html" : "http://127.0.0.1:8000/api/v1/reportes/file/{}/{}.html".format(reporet, reporet),
    }
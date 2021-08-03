from pydantic import BaseModel, HttpUrl, Field

class Reportes(BaseModel):
    ip: str
    port: int = 27017
    user: str
    password: str
    db: str
    collection: str
    query: dict
    skip : int = 0
    limit : int = 100
    namereport: str
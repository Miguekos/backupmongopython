from pydantic import BaseModel, HttpUrl, Field

class Listar(BaseModel):
    ip: str
    port: str = "27017"
    user: str = ""
    password: str = ""

class Backup(Listar):
    db: str = Field(None, description="Debes definir el nombre de la base de datos", min_length=1)

class BackupRestore(Listar):
    db: str = Field(None, description="Debes definir el nombre de la base de datos", min_length=1)
    ip_rest: str
    port_rest: str = "27017"
    user_rest: str = ""
    password_rest: str = ""
    db_rest: str
    restore: bool = False
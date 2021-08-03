from fastapi.responses import FileResponse
from .logic import restore_db, backup_db, listar_db
from .models import Listar, Backup, BackupRestore
from datetime import datetime, time, timedelta
from fastapi import APIRouter, Depends, HTTPException
# from socker_cliente import enviarprueba
# from main import socket_manager as sm
# import socketio
# sio = socketio.AsyncClient()
# @sm.on('leave')
# async def handle_leave(sid, *args, **kwargs):
#     await sm.emit('lobby', 'User left')

from fastapi import WebSocket
# import socketio
# sio = socketio.AsyncClient()

# async def inicio_sock():
#     await sio.connect('http://localhost:7667')
#     # await sio.connect('http://localhost:7667', transports='websocket', socketio_path='/socketimpresora')
#     return await sio.wait()
# def asd():
#     print("asdadasdadasdasd")
# @sio.event
# async def connect():
#     print('connection established')
#     await sio.emit('myresponse', {'response': 'my response'})
#     await sio.emit('backend_recibed', {'response': 'my response'})
#
# @sio.event
# def disconnect():
#     print('disconnected from server')
#
# @sio.event
# async def my_message(data):
#     print('message received de ', data)


backup_restore_router = APIRouter()

# asd = "asdadasdadasdasd"

# async def dddd():
#     print("ejecutando dddd")
#     # return "dfgsfgsdfg"
#     await sio.connect('http://localhost:7667')
#     print("2")
#     # await sio.connect('http://localhost:7667', transports='websocket', socketio_path='/socketimpresora')
#     socsio = await sio.wait()
#     print("3")
#     print("socsio", socsio)

@backup_restore_router.get("/send")
async def send():
    try:
        print("enviar_front")
        # await enviarprueba()
        # await enviar_front("enviar_front")
    except:
        print("except")
        pass
        # return {"message": "Su archivo {} ya no existe".format(name)}

@backup_restore_router.get("/file/{name}")
async def file(name):
    try:
        return FileResponse("./tmp/{}".format(name))
    except:
        return {"message": "Su archivo {} ya no existe".format(name)}


@backup_restore_router.post("/backup")
async def backup(backup: Backup):
    print("backup", backup)
    back_up_dict = backup.dict()
    # print(back_up_dict["db"])
    backup_db(back_up_dict)
    fecha = datetime.now().strftime("%Y_%m_%d")
    return {
        "url": "http://95.111.235.214:3064/file/{}_{}.zip".format(back_up_dict["db"], fecha)
    }


@backup_restore_router.post("/backuprestore")
async def backuprestore(backup: BackupRestore):
    try:
        back_up_dict = backup.dict()
        bac = backup_db(back_up_dict)
        # print("bac", bac)
        if back_up_dict['restore']:
            res = restore_db(back_up_dict)
            # print("res", res)
            fecha = datetime.now().strftime("%Y_%m_%d")
            return {
                # "url": "http://95.111.235.214:3064/file/{}_{}.zip".format(back_up_dict["db"], fecha),
                "url": bac,
                "restore" : res if res != None else "No existe"
            }
        else:
            return {
                # "url": "http://95.111.235.214:3064/file/{}_{}.zip".format(back_up_dict["db"], fecha),
                "url": bac,
                "restore": "false"
            }
    except Exception as e:
        return {
            # "url": "http://95.111.235.214:3064/file/{}_{}.zip".format(back_up_dict["db"], fecha),
            # "url": bac,
            "datail": e
        }

@backup_restore_router.post("/restore")
async def restore(backup: BackupRestore):
    try:
        back_up_dict = backup.dict()
        # bac = backup_db(back_up_dict)
        # print("bac", bac)
        if back_up_dict['restore']:
            res = restore_db(back_up_dict)
            # print("res", res)
            fecha = datetime.now().strftime("%Y_%m_%d")
            return {
                # "url": "http://95.111.235.214:3064/file/{}_{}.zip".format(back_up_dict["db"], fecha),
                # "url": bac,
                "restore" : res if res != None else "No existe"
            }
        else:
            return {
                # "url": "http://95.111.235.214:3064/file/{}_{}.zip".format(back_up_dict["db"], fecha),
                # "url": bac,
                "restore": "false"
            }
    except ValueError as e:
        return {
            # "url": "http://95.111.235.214:3064/file/{}_{}.zip".format(back_up_dict["db"], fecha),
            # "url": bac,
            "datail": e
        }

@backup_restore_router.post("/listarTablas")
async def listarTablas(listar: Listar):
    print(listar)
    db = listar_db(listar.dict())
    return db

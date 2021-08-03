from queue import Queue
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from controllers.backup_restore.routes import backup_restore_router
from controllers.reportes.routes import reportes_router
# from socker_cliente import iniciar
app = FastAPI()
# queue = Queue()
# from fastapi_socketio import SocketManager
# import socketio
# sio = socketio.AsyncClient()
# import socketio
# sio = socketio.AsyncClient(logger=True, engineio_logger=True)
# sio = socketio.AsyncClient()

# from controllers.backup_restore

# @sio.event
# async def connect():
#     print('connection established')
#     await sio.emit('myresponse', {'response': 'my response'})
#     await sio.emit('backend_recibed', {'response': 'my response'})

# async def main():
#     await sio.connect('http://localhost:7667')
#     # await sio.connect('http://localhost:7667', transports='websocket', socketio_path='/socketimpresora')
#     return await sio.wait()

# async def enviar_front(val):
#     await sio.emit('backend_recibed', val)
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

# socket_manager = SocketManager(app=app)

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("ws ws ws")
#     while True:
#         msg = queue.get()
#         await websocket.send_json(data=msg)


# @app.put("/dummy")
# async def update(dummy):
#     queue.put(dummy)

# app = FastAPI()
# sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
# sio_asgi_app = socketio.ASGIApp(sio)

# sio = socketio.AsyncServer(async_mode='asgi')
# sio_asgi_app = socketio.ASGIApp(sio, app, socketio_path="/api/socket.io")
# app.mount("/", sio_asgi_app)
# sio = socketio.AsyncServer(async_mode='asgi')
# sio_asgi_app = socketio.ASGIApp(sio, app)

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
    "http://gps.test/"
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# sio = SocketManager(app=app, cors_allowed_origins=["*"])

app.include_router(
    backup_restore_router,
    prefix="/api/v1/backuprestore",
    tags=["backuprestore"],
    responses={
        404: {
            "description": "Not found"
        }
    }
)

app.include_router(
    reportes_router,
    prefix="/api/v1/reportes",
    tags=["reportes"],
    responses={
        404: {
            "description": "Not found"
        }
    }
)
#
# @sio.on('connect')
# async def connect():
#     print('connect')

@app.on_event("startup")
async def app_startup():
    """
    Do tasks related to app initialization.
    """
    # instacia = await inicio_sock()
    # try:
        # await dddd()
        # await iniciar()
        # print("1")
        # await sio.connect('http://localhost:7667')
        # print("2")
        # # await sio.connect('http://localhost:7667', transports='websocket', socketio_path='/socketimpresora')
        # socsio = await sio.wait()
        # print("3")
        # print("socsio", socsio)
    # except Exception as e:
    #     print("Socket error: ",e)
    # print("instacia", instacia)
    # This if fact does nothing its just an example.
    # config.load_config()
    # print("startup")


@app.on_event("shutdown")
async def app_shutdown():
    """
    Do tasks related to app termination.
    """
    # This does finish the DB driver connection.
    # config.close_db_client()
    # print("shutdown")

# https://user-images.githubusercontent.com/36239763/103555401-80614100-4eb0-11eb-91e9-a9a5552c4c10.png
# uvicorn main:app --host "0.0.0.0" --port 8000 --log-level "info" --reload



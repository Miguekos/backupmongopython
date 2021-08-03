# import socketio
# sio = socketio.AsyncClient()
#
#
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
#
#
# async def iniciar():
#     await sio.connect('http://localhost:7667')
#     await sio.wait()
#
#
# async def enviarprueba():
#     await sio.emit('myresponse', {'response': 'my response'})
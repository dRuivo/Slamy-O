import socketio
from threading import Thread

sio = socketio.Client()

class slamyoClient(socketio.ClientNamespace):
    def on_connect(self):
        print('connection established')

    def on_disconnect(self):
        print('disconnected from server')

sio.register_namespace(slamyoClient())

"""
@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')
"""


try:
    sio.connect('http://localhost:5000')
    while True:
        pass
    #sio.wait()

except KeyboardInterrupt:
    print("disconnecting")
    sio.disconnect()
import socketio
from numpy import sin, cos, pi, floor
from adafruit_rplidar import RPLidar

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

# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME)

#pylint: disable=redefined-outer-name,global-statement
def process_data(data):
    points = []
    for angle in range(360):
        distance = data[angle]
        if distance > 0:                  # ignore initially ungathered data points
            radians = angle * pi / 180.0
            x = distance * cos(radians)
            y = distance * sin(radians)
            points.append({"x": x, "y":y})
    sio.emit("lidar_data", points)

  
scan_data = [0]*360

try:
    sio.connect('http://localhost:5000')
    print(lidar.info)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, int(floor(angle))])] = distance
        process_data(scan_data)

except KeyboardInterrupt:
    print("disconnecting")
sio.disconnect()
lidar.stop()
lidar.disconnect()

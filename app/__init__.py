from flask import Flask, render_template
from flask_socketio import SocketIO, Namespace, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


class slamysock(Namespace):
    def on_connect(self):
        #request.sid
        print('got connection')

    def on_disconnect(self):
        print('got disconnection')

    def on_lidar_data(self, data):
        emit('lidar_data', data, broadcast =True)
        #print(data)

    def on_my_event(self, json):
        print('received json: ' + str(json))

socketio.on_namespace(slamysock('/'))

if __name__ == '__main__':
    socketio.run(app)
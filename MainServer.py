import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def execute_search(sid, data):
    print(sid, data)
    sio.emit('reply', {'response': data}, room=sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 12345)), app)




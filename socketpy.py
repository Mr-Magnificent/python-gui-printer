import socketio
import subprocess
import base64
import win32print

sio = socketio.Client()
sio.connect('http://localhost:3000')

@sio.on('connect')
def on_connect():
    # Write code for connected on('add user') with uuid and alias
    # for on_reconnect
    print("connected!")

    with open('credentials.txt', 'r') as file:
        cred = file.readlines()
        print(cred)



@sio.on('pdfData')
def on_message(data):
    try:
        print(data.keys(), type(data['pdf']))
        data_rec = bytearray(base64.b64decode(data['pdf']))
        with open("output.ps", "wb") as file:
            file.write(data_rec)

        # Write code to take print out below
        
    except BaseException as e:
        print("in except", str(e))

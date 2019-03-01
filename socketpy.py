import base64
import subprocess
import test
import uuid

import socketio

import win32print

sio = socketio.Client()
sio.connect('http://192.168.31.12:3000')

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
        filename = str(uuid.uuid4())
        with open("{0}.ps".format(filename), "wb") as file:
            file.write(data_rec)

        test.generatePrint(filename)
        # Write code to take print out below
        
    except BaseException as e:
        print("in except", str(e))

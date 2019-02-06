import socketio
import subprocess
import base64
print("Hello")

sio = socketio.Client()
sio.connect('http://localhost:3000')


@sio.on('pdfData')
def on_message(data):
    try:
        print(data.keys(), type(data['pdf']))
        data_rec = bytearray(base64.b64decode(data['pdf']))
        with open("output.ps", "wb") as file:
            file.write(data_rec)

        # Write code to take print out below
        subprocess.run([f'find . | grep output.ps'])
    except BaseException as e:
        print("in except", str(e))

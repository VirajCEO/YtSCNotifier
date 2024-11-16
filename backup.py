from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import threading
app = Flask(__name__)
socketio = SocketIO(app)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')


def send_data():
    while True:
        input("Enter")
        socketio.emit('message', {"action": "update", "message": "Yooooooo my name is viraj i am from ghar myself and testing and Aloxen atuomations","name":"DemonBHaii","amount":'Donated ₹200'})



if __name__ == "__main__":
    threading.Thread(target=send_data).start()
    socketio.run(app, host='localhost', port=8765)




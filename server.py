from flask import Flask, request, redirect,jsonify
import hmac
import hashlib
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import threading
app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return redirect('https://rzp.io/l/aloxen') 

@app.route('/notify')
def notifier():
    return render_template('index.html')


def verify_signature(payload, signature, secret):
    """Verify Razorpay webhook signature."""
    generated_signature = hmac.new(
        key=secret.encode('utf-8'),
        msg=payload.encode('utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(generated_signature, signature)


def send_notification(message):
    """Function to send notifications to clients."""
    data = message
    payment_id = data['payload']['payment']['entity']['id']
    amount = data['payload']['payment']['entity']['amount']
    currency = data['payload']['payment']['entity']['currency']
    amount = amount//100
    name = data['payload']['payment']['entity']['notes']['name']
    message = data['payload']['payment']['entity']['notes']['your_message']
    final_data = {
        'name' : name,
        'amount' :amount,
        'message' :message,
        'payment_id' : payment_id
    }
    socketio.emit('message', {"action": "update", "message": message,"name":name,"amount":f'Donated ₹{amount}'})


@app.route('/donate')
def donate():
    return redirect('https://rzp.io/l/aloxen')

@app.route('/rp-gateway', methods=['POST'])

def razorpay_webhook():
    """Webhook endpoint to handle Razorpay notifications."""
    webhook_data = request.get_json()
    send_notification(webhook_data)
    return jsonify({'status': 'success'}), 200


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')





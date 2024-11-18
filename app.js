const express = require('express');
const crypto = require('crypto');
const fs = require('fs');
const https = require('https');
const http = require('http');
const { Server } = require('socket.io');

const app = express();


app.use('/css', express.static(path.join(__dirname, '../public/css')));

app.use('/vids', express.static(path.join(__dirname, '../public/vids')));

// SSL certificate paths
const privateKey = fs.readFileSync('/etc/letsencrypt/live/aloxen.in/privkey.pem', 'utf8');
const certificate = fs.readFileSync('/etc/letsencrypt/live/aloxen.in/cert.pem', 'utf8');
const ca = fs.readFileSync('/etc/letsencrypt/live/aloxen.in/chain.pem', 'utf8');

const credentials = { key: privateKey, cert: certificate, ca: ca };

// Middleware for parsing JSON requests
app.use(express.json());

// Redirect to donation link
app.get('/', (req, res) => {
  res.redirect('https://rzp.io/l/aloxen');
});

// Render the notification page
app.get('/notify', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});


// Function to send notifications to clients
function sendNotification(data) {
  const paymentId = data.payload.payment.entity.id;
  const amount = data.payload.payment.entity.amount / 100;
  const name = data.payload.payment.entity.notes.name;
  const message = data.payload.payment.entity.notes.your_message;

  console.log('Sending data:', { name, amount, message });
  io.emit('message', {
    action: 'update',
    name,
    amount: `Donated ₹${amount}`,
    message,
  });
}

// Razorpay webhook endpoint
app.post('/rp-gateway', (req, res) => {
  const webhookData = req.body;
  const payload = JSON.stringify(webhookData);
  const signature = req.headers['x-razorpay-signature'];
  console.log('WEB HOOK DATA : ');
  console.log(webhookData);
  sendNotification(webhookData);
  res.json({ status: 'success' });

});

// HTTPS server setup
const httpsServer = https.createServer(credentials, app);
const io = new Server(httpsServer);

// Socket.io connection
io.on('connection', (socket) => {
  console.log('Client connected');
  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

// Start the server
const PORT = process.env.PORT || 443;
httpsServer.listen(PORT, () => {
  console.log(`HTTPS server running on https://aloxen.in:${PORT}`);
});

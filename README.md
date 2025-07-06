# YtSCNotifier – Free Razorpay Donation Alerts for Streamers

**YtSCNotifier** is a self-hosted, real-time **Razorpay donation alert system** built for **small streamers** (especially those under 500 subscribers) who aren't eligible for YouTube SuperChat.

With YtSCNotifier, you get:

* Live on-stream notifications when someone donates via Razorpay
* Customizable video & sound alerts
* Full control via your Razorpay dashboard
* Custom UI – edit the `index.html` to match your stream's vibe

---

## Features

* Real-time donation alerts using Socket.IO
* Fully secure with HTTPS and SSL certificates
* Plays random video alerts from your chosen folder
* Easy to customize how the donation popup looks
* Link directly from your website or stream overlay

---

## Prerequisites

* A domain (e.g., `yourdomain.com`)
* SSL certificates (e.g., via Let's Encrypt)
* Node.js + NPM
* A public Razorpay account with Webhook access
* A server (AWS/GOOGLE-CLOUD)

---

## Folder Structure

```
.
├── public/
│   ├── css/             # Your styles
│   └── vids/            # Your custom alert videos (.mp4)
├── index.html           # Notification UI (edit as you wish)
├── server.js            # Main backend logic
```

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/YtSCNotifier.git
cd razornotify
```

2. Install dependencies

```bash
npm install
```

3. Place your alert videos

Put your `.mp4` videos inside the `/public/vids/` folder.

4. Set up SSL certificates

Make sure your domain has valid SSL certs, then update the paths in `server.js`:

```js
const privateKey = fs.readFileSync('/etc/letsencrypt/live/yourdomain.com/privkey.pem');
const certificate = fs.readFileSync('/etc/letsencrypt/live/yourdomain.com/cert.pem');
const ca = fs.readFileSync('/etc/letsencrypt/live/yourdomain.com/chain.pem');
```

5. Start the server

```bash
sudo node server.js
```

6. Expose the notification page on your stream

Add `https://yourdomain.com/notify` as a **Browser Source** in OBS or Streamlabs.

---

## Testing Locally (without HTTPS)

Skip SSL setup and run using HTTP on port `80`. Replace the `httpsServer` setup with a simple HTTP server if needed.

---

## Razorpay Setup

1. Go to **Razorpay Dashboard > Settings > Webhooks**
2. Add a webhook URL:

   ```
   https://yourdomain.com/rp-gateway
   ```
3. Enable the `payment.paid` event
4. In your payment links, include custom fields:

   * `name`
   * `your_message`

---

## Customization

* Change how the popup looks in `index.html`
* Use your own fonts, styles, and sounds
* Add overlays or emojis
* Modify `random_video` logic to map videos to amounts, names, etc.

---

## Security Notes

* Use HTTPS in production.
* Whitelist Razorpay IPs if you're worried about spoofed webhook calls.
* You can add HMAC verification for the webhook payload (optional upgrade).

---

## Why This Exists

For small streamers, Razorpay is a great way to receive donations – but it lacked a real-time alert system like SuperChat.
**RazorNotify fills that gap — 100% free and open source.**

---

## Contribute

Feel free to fork, improve, or create pull requests. Add styling, audio support, or dashboard stats.

---

## License

MIT License – Use it, tweak it, share it however you like ;)

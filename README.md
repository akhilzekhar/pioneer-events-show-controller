# Pioneer Events Show Controller

> ⚠️ This was an experimental project built for a specific live event. It is not a polished product — it was a real solution built on the fly for a real show floor.

A browser-based show control panel operated from an iPad or Android tablet. Built for the **Pioneer Events** show featuring Al Hilal content in Saudi Arabia. Pressing a button on the tablet triggers a UDP command to Bitfocus Companion, which fires the corresponding video cue — while a dedicated display page shows the scene title, description, and a real-time progress bar synced to the video timer.

---

## How It Works

```
Tablet (Browser) → Flask Server → UDP → Bitfocus Companion → Video Playback
```

1. Operator taps a button on the tablet
2. Browser sends an HTTP request to the Flask server (`server.py`)
3. Flask forwards a UDP command to Bitfocus Companion on the target port
4. Companion triggers the video cue
5. Browser navigates to `display.html` showing scene info + countdown progress bar
6. After the timer expires, the interface auto-returns to the main menu

---

## Pages

| File | Purpose |
|---|---|
| `index.html` | Main control panel — 5 scene buttons + standby |
| `display.html` | Scene display page with title, description, and progress bar |
| `standby.html` | Standby screen with rotating logo — click anywhere to return |
| `styles.css` | Shared styles across all pages |
| `server.py` | Flask server — receives HTTP requests, sends UDP to Companion |

---

## Scenes

| Button | UDP Command | Video Timer |
|---|---|---|
| INTRO | `LOCATION 1/0/0 PRESS` | 73s |
| BIDDING NATION 2034 | `LOCATION 1/0/1 PRESS` | 68s |
| PROPTECH | `LOCATION 1/0/2 PRESS` | 114s |
| AL HILAL MUSEUM | `LOCATION 1/0/3 PRESS` | 51s |
| AL HILAL x PIONEER EVENTS | `LOCATION 1/0/4 PRESS` | 65s |
| STANDBY | `LOCATION 1/0/5 PRESS` | — |

---

## Setup

**Requirements:**
- Python 3
- Flask + flask-cors (`pip install flask flask-cors`)
- Bitfocus Companion running on the same or networked machine

**Run the server:**
```bash
python server.py
```

**Configure:**

In `server.py`, set the target IP and port:
```python
TARGET_IP = '127.0.0.1'  # IP of the machine running Companion
TARGET_PORT = 5001
```

In `index.html`, set the Flask server IP:
```javascript
const url = `http://YOUR_SERVER_IP:5000/udp?command=...`
```

Open `index.html` in a browser on the tablet. Both the tablet and the server must be on the same network.

---

## Features

- Fade transitions between all pages
- Auto-standby after 30 seconds of inactivity on the main menu
- Per-scene auto-return timer synced to video length
- Real-time progress bar depleting as the video plays
- Responsive layout — works on iPad and Android tablets
- Standby screen with rotating logo

---

## Stack

- HTML / CSS / JavaScript (vanilla)
- Python / Flask
- UDP sockets
- Bitfocus Companion

---

## Notes

This was built quickly for a specific event and iterated on the show floor. The IP addresses and UDP commands are hardcoded for that setup. If you want to adapt it for your own show, update the IPs in `server.py` and `index.html`, and adjust the Companion button locations and timers to match your project.

# Pioneer Events Show Controller  

> ⚠️ **Experimental Project** — Built and tested for a live event production. Not a polished product, but it worked on the show floor.

A browser-based show control panel designed to be operated from a tablet (iPad or Android) during a live event. Pressing a button triggers a UDP command to Bitfocus Companion, which controls the media server — while simultaneously displaying the scene title and description on a secondary screen, with a real-time progress bar synced to the video clip duration.

---

## How It Works

```
Tablet (browser) → Flask Server → UDP → Bitfocus Companion → Media Server
                       ↓
                 Display Page (scene info + progress bar)
```

1. Operator opens `index.html` on a tablet
2. Taps a scene button (e.g. INTRO, PROPTECH, AL HILAL MUSEUM)
3. Flask server sends a UDP command to Bitfocus Companion
4. Companion triggers the corresponding cue on the media server
5. Browser navigates to `display.html` showing the scene name, description, and a countdown progress bar
6. After the clip ends, the interface auto-returns to `index.html`
7. If idle for 30 seconds, the interface fades to a standby screen with a rotating logo

---

## Files

| File | Purpose |
|---|---|
| `index.html` | Main control panel — scene buttons |
| `display.html` | Per-scene display with progress bar |
| `standby.html` | Idle/standby screen with rotating logo |
| `styles.css` | Shared styles across all pages |
| `server.py` | Flask server that receives HTTP requests and forwards as UDP |
| `A.png` | Pioneer Events logo (used on standby screen) |

---

## Scenes

| Button | UDP Command | Video Duration |
|---|---|---|
| INTRO | `LOCATION 1/0/0 PRESS` | 73s |
| BIDDING NATION 2034 | `LOCATION 1/0/1 PRESS` | 68s |
| PROPTECH | `LOCATION 1/0/2 PRESS` | 114s |
| AL HILAL MUSEUM | `LOCATION 1/0/3 PRESS` | 51s |
| AL HILAL x PIONEER EVENTS | `LOCATION 1/0/4 PRESS` | 65s |
| STANDBY | `LOCATION 1/0/5 PRESS` | — |

---

## Setup

### Requirements
- Python 3
- Flask
- flask-cors

```bash
pip install flask flask-cors
```

### Run the server
```bash
python server.py
```
Server runs on `http://0.0.0.0:5000`

### Configure
In `server.py`, set your Bitfocus Companion machine IP and port:
```python
TARGET_IP = '127.0.0.1'   # IP of the machine running Companion
TARGET_PORT = 5001         # Companion UDP port
```

In `index.html`, set your server IP:
```javascript
const url = `http://YOUR_SERVER_IP:5000/udp?command=...`
```

### Open on tablet
Open `index.html` in a browser on any device on the same network.

---

## Built With

- HTML / CSS / JavaScript — frontend
- Python + Flask — UDP bridge server
- Bitfocus Companion — show control middleware
- Operated on iPad / Android tablet

---

## Context

Built as a personal experiment to explore whether a standard browser on a tablet could replace a dedicated show controller in a live event setup. The event content (Pioneer Events, Al Hilal Museum, FIFA World Cup 2034 bid) is fictional — used purely as realistic example data to simulate how the system would behave in a real production environment.

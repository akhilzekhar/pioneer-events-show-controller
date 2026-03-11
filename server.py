from flask import Flask, request, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Configuration for the target device
TARGET_IP = '127.0.0.1' # Replace with your target device's IP address
TARGET_PORT = 5001      # <--- CHANGE THIS TO 5001
# TARGET_IP will likely need to be the actual IP of the machine running Companion,
# unless Companion is on the same machine as this Flask server.
# If Companion is on the same machine, '127.0.0.1' is fine.
# If on another machine, find that machine's local IP (e.g., 192.168.1.XX)

@app.route('/udp', methods=['GET'])
def send_udp():
    command = request.args.get('command')
    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Send the command
        sock.sendto(command.encode('utf-8'), (TARGET_IP, TARGET_PORT))
        
        # Close the socket
        sock.close()
        
        print(f"UDP command '{command}' sent to {TARGET_IP}:{TARGET_PORT}")
        return jsonify({'status': 'success', 'command': command}), 200
    except Exception as e:
        print(f"Error sending UDP command: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on http://localhost:5000
    app.run(host='0.0.0.0', port=5000)
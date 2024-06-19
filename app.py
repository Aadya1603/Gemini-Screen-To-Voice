from flask import Flask, request, send_from_directory
import threading
import subprocess
import json

app = Flask(__name__)

# Event to signal stopping the voice app
stop_event = threading.Event()
api_key = ''

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/styles.css')
def serve_css():
    return send_from_directory('.', 'styles.css')

@app.route('/start-application', methods=['POST'])
def start_application():
    global api_key
    data = request.get_json()
    api_key = data['apiKey']
    if not stop_event.is_set():
        stop_event.clear()
        threading.Thread(target=start_voice_app).start()
        return "Application started successfully!", 200
    else:
        return "Application is already running.", 200

@app.route('/stop-application')
def stop_application():
    stop_event.set()
    return "Application stopped successfully!", 200

def start_voice_app():
    while not stop_event.is_set():
        subprocess.run(["python", "voice.py", api_key])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

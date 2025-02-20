from flask import Flask
import os
import datetime
import subprocess
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask Server Running</h1><p>Go to <a href='/htop'>/htop</a> to see system details.</p>"

@app.route('/htop')
def htop():
    name = "RAKESH D"
    username = os.getenv("USERNAME") or os.getenv("USER") or "codespace"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime('%Y-%m-%d %H:%M:%S')

    if platform.system() == "Linux":
        top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout
    else:
        top_output = subprocess.run(["tasklist"], capture_output=True, text=True).stdout  # For Windows

    return f"""
    <h1>Name: {name}</h1>
    <p>User: {username}</p>
    <p>Server Time (IST): {formatted_time}</p>
    <pre>Top Output:<br>{top_output}</pre>
    """

@app.route('/favicon.ico')
def favicon():
    return "", 204  # Empty response with HTTP 204 (No Content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

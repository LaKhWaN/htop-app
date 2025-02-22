from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # creating a simple route to return a simple html
    full_name = "Upender Singh Lakhwan"
    system_username = os.getenv("USER") or os.getenv("USERNAME")
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -b -n 1 | head -n 10")

    return f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {system_username}</p>
    <p><b>Server Time (IST):</b> {ist_time}</p>
    <pre><b>Top Output:</b>\n{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

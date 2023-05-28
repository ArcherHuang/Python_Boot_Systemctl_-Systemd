import os
import json
from flask import Flask

base_path = "/home/mmosconii"

f = open(f"{base_path}/Python_Boot_Systemctl_Systemd/data.json")
data = json.load(f)
f.close()

app = Flask(__name__)

@app.route('/')
def hello():
    return data['message']
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
import os
import json
from flask import Flask

whoami = os.system("whoami")
print(f"whoami: {whoami}")

f = open('./data.json')
data = json.load(f)
f.close()

app = Flask(__name__)

@app.route('/')
def hello():
    return data['message']
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
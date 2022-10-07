import socket
from flask import Flask, flash, request
from flask import jsonify
from flask_cors import CORS
from ec2_metadata import ec2_metadata
import uuid
app = Flask(__name__)
CORS(app)
@app.route('/systemdetails', methods=['GET'])
def system():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    d = {"Host Name": hostname,
         "IP Address": IPAddr,
         "Mac Address": hex(uuid.getnode()),
         "Instance ID": ec2_metadata.instance_id}
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    return jsonify(d)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
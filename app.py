from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/ls/<path:lsPath>', methods=['GET'])
def list(lsPath):
    output = subprocess.check_output(['ls', '-l', '/' +lsPath])
    return '<pre>' + output.decode() + '</pre>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

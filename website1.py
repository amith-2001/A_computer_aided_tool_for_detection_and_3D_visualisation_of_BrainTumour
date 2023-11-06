
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from flask_ngrok import run_with_ngrok
app = Flask(__name__)

@app.route('/data',methods=['POST','GET'])
def do_pred():
    if request.method == 'GET':
        x = input('\n enter :')
        return x



if __name__ == '__main__':
    app.run(host='192.168.43.156', port=5000)
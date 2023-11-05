from flask import Flask
import threading
import logging
import sys

# Disable Flask's default startup message
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)


@app.route('/')
def home():
  return '<h1 style="text-align: center; position: absolute; top: 30%; left: 50%; transform: translate(-50%, -50%); font-size: 250px;">Welcome</h1>'


def run_flask():
  app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
  # Run the Flask server in a separate thread
  threading.Thread(target=run_flask).start()
  exec(open("main.py").read())

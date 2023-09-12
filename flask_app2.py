from kiteconnect import KiteConnect
from flask import Flask, request, render_template_string, redirect, url_for
import json
import threading

app = Flask(__name__)

with open('config.json', 'r') as file:
    config = json.load(file)

api_key = config['KITE_API_KEY']
api_secret = config['KITE_API_SECRET']

kite = KiteConnect(api_key=api_key)

# Template for the main page with the "Login with Kite" button
index_template = """
<html>
    <body>
        <a href="{{ login_url }}"><button>Login with Kite</button></a>
    </body>
</html>
"""

# Template for the success page
success_template = """
<html>
    <body>
        <h2>Authentication successful!</h2>
    </body>
</html>
"""

# Template for the failure page
failure_template = """
<html>
    <body>
        <h2>Authentication failed!</h2>
    </body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(index_template, login_url=kite.login_url())


@app.route("/redirect")
def redirect_url():
    request_token = request.args.get('request_token')
    if not request_token:
        return render_template_string(failure_template)

    try:
        data = kite.generate_session(request_token, api_secret=api_secret)
        kite.set_access_token(data["access_token"])
        return redirect(url_for('success'))
    except Exception as e:
        return redirect(url_for('failure'))


@app.route("/success")
def success():
    return render_template_string(success_template)


@app.route("/failure")
def failure():
    return render_template_string(failure_template)


def run_flask_app():
    app.run(port=5010)


# Start the Flask app in a separate thread
threading.Thread(target=run_flask_app).start()

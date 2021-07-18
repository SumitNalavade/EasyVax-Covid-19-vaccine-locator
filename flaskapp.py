from flask import Flask, render_template, request
import vaxfinder

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home_page():
    return render_template("index.html")


@app.route('/send', methods=['POST'])
def send():
    if(request.method == 'POST'):
        address = request.form['address']

        location_array = vaxfinder.find(address)

        return(render_template('index.html', location_array=location_array))

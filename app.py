from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

# Create the main route / with GET and POST handling
@app.route('/', methods=['GET', 'POST'])
def index():
    ...


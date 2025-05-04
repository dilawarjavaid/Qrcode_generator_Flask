from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

# Create the main route / with GET and POST handling
@app.route('/', methods=['GET', 'POST'])
def index():
    text = request.form['text']
    # Generate QR code using qrcode library
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    #Save the QR image to an in-memory buffer
    buffer = BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='qrcode.png')





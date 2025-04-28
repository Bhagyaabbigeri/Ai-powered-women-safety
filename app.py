from flask import Flask, render_template, request
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')

    # Load credentials from environment
    account_sid = os.getenv('TWILIO_SID')
    auth_token = os.getenv('TWILIO_TOKEN')
    twilio_number = os.getenv('TWILIO_NUMBER')
    to_number = os.getenv('RECIPIENT_NUMBER')

    client = Client(account_sid, auth_token)

    google_maps_link = f"https://www.google.com/maps?q={lat},{lon}"

    message = client.messages.create(
        body=f"🚨 Emergency! I need help. My location: {google_maps_link}",
        from_=twilio_number,
        to=to_number
    )

    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

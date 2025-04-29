from flask import Flask, render_template, request
from twilio.rest import Client
from dotenv import load_dotenv
import os

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

    print(f"[+] Received location: Latitude={lat}, Longitude={lon}")

    # Twilio credentials from .env
    account_sid = os.environ.get("TWILIO_SID")
    auth_token = os.environ.get("TWILIO_TOKEN")
    twilio_number = os.environ.get("TWILIO_NUMBER")
    to_number = os.environ.get("RECIPIENT_NUMBER")

    client = Client(account_sid, auth_token)

    google_maps_link = f"https://www.google.com/maps?q={lat},{lon}"

    message = client.messages.create(
        body=f"🚨 Emergency! I need help. My location: {google_maps_link}",
        from_=twilio_number,
        to=to_number
    )

    print(f

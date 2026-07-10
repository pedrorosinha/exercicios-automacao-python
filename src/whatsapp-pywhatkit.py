import pywhatkit
from datetime import datetime, timedelta

agora = datetime.now() + timedelta(minutes=1)

country_code = input("Enter the country code (e.g., +1 for USA): ")
phone_number = input("Enter the phone number: ")
message = input("Enter the message: ")

pywhatkit.sendwhatmsg(f"+{country_code}{phone_number}", message, agora.hour, agora.minute, 5, True, 2)
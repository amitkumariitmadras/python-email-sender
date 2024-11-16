import os
from dotenv import load_dotenv

load_dotenv()
# just checking for signed commits and co-authored

smtp_server = os.getenv('ADDRESS')
smtp_port = os.getenv('PORT')
sender_email = os.getenv('EMAIL')
sender_password = os.getenv('PASSWORD')

print(smtp_server, sender_email, sender_password, smtp_port)
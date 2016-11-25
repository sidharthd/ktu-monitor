from flask import Flask
from time import sleep
import notification

def send_mail(notifications):
	for i in notifications:
		print(i)

app = Flask(__name__)

last_notification = ""
while(1):
	notificaions = notification.search(last_notification)
	if notificaions:
		last_notification = notificaions[0]
		send_mail(notificaions)
	else:
		print("Nothing new :(")
	sleep(5)

@app.route("/")
def index():
	return "Hello world!"
from bs4 import BeautifulSoup as bs
import requests
from time import sleep

def send_mail(notifications):
	for i in notifications:
		print(i)

last_notification = ""

while(1):
	url = "https://ktu.edu.in/eu/core/announcements.htm"
	r=requests.get(url)
	
	html=r.text
	soup=bs(html,"html.parser")

	rows = soup.find(class_="ktu-news").find_all("tr")

	notifications = []

	for row in rows:
		notification = row.find_all("td")[1].find("b").text
		if notification != last_notification:
			notifications.append(notification)
		else:
			break

	if notifications:
		last_notification = notifications[0]
		send_mail(notifications)
	else:
		print("No new notifications!")

		sleep(5)
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url = 'https://www.npr.org/sections/news/'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
articles = soup.find_all('article', class_='item')
headlines = [article.h2.a.text.strip() for article in articles]

print('NPR News Headlines:')
for headline in headlines:
    print('- ' + headline)

from_address = 'your_email_address@example.com'
to_address = 'recipient_email_address@example.com'
subject = 'NPR News Headlines'
body = '\n'.join('- ' + headline for headline in headlines)

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(from_address, 'your_email_password')
text = msg.as_string()
smtp_server.sendmail(from_address, to_address, text)
smtp_server.quit()

print('Email sent successfully.')

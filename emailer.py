import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "email you want to send from"
receiver_email = "email you want to send to"
password = "16 digits password from google account"

message = MIMEMultipart("alternative")
message["Subject"] = "Automated Email from Python"
message["From"] = sender_email
message["To"] = receiver_email

text = "Hello,\nThis is an automated email sent from Python."
html = """\
<html>
<body>
<p>Hello,</p>
<p>This will be an <b>automated email</b> sent using Python.</p>
</body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

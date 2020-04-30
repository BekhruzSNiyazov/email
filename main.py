import smtplib

server = input("Which server are you using (gmail, outlook): ")
_from = input("Type your email address: ")
password = input("Type your password: ")
to = input("Send to: ")
subject = input("Subject: ")
body = input("Body: ")
message = f"""\
Subject: {subject}

{body}
"""
server = smtplib.SMTP(f"smtp.{server}.com", 587)
server.starttls()
server.login(_from, password)
server.sendmail(_from, to, message)
print("Sent.")

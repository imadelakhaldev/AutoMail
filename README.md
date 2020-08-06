# AutoMail
## Efficient, easy to use Python class/package to send emails using SMTP.

Import this class to your project to send bulk or individual plain text or HTML emails with attachment.
Pass your own SMTP server credentials while making an instance of this class.
You can use Google Gmail server to send emails ("smtp.gmail.com", 465, YOUR_EMAIL, YOUR_PASSWORD)

```
Start connection to the SMTP server.
hostname = SMTP server host.
port_num = SMTP server port number.
username = SMTP login username.
password = SMTP login password.
```

```
check_status() method.
Check the SMTP server status.
Return true if SMTP server status is connected.
Return false if SMTP server status is not connected.
```

```
reconnect() method.
Establish a new SMTP connection to the server using new credentials.
hostname = SMTP server host.
port_num = SMTP server port number.
username = SMTP login username.
password = SMTP login password.
```

```
add_message() method.
Add an email template to be sent later.
subject = Email subject.
content = Plain text email content.
html (optional) = HTML content to be added to the email template.
```

```
add_attachment method.
Add a file a attachment to the email template to be sent later.
full_path = Full path to the file.
```

```
send_message() method.
Send email using added email template and attachments.
sender = From email address.
receiver = To email address.
```

```
send_messages() method.
Send bulk emails using added email template and attachments.
sender = From email address.
receivers = To email addresses.
```

Basic email example.
```
from automail import AutoMail

bot = AutoMail("smtp.gmail.com", 465, "example@gmail.com", "123example")
bot.add_message("This is a subject", "This is a content")
bot.add_attachment("/Users/exampleuser/Desktop/report.pdf")
bot.send_message("example@gmail.com", "terry-davis@templeos.org")
```

HTML email example
```
from automail import AutoMail

bot = AutoMail("smtp.gmail.com", 465, "example@gmail.com", "123example")
bot.add_message("This is a subject", "This is a content", "<h1>This is a subject</h1><p>This is a content</p>")
bot.add_attachment("/Users/exampleuser/Desktop/report.pdf")
bot.send_message("example@gmail.com", "terry-davis@templeos.org")
```

Bulk HTML email example
```
from automail import AutoMail

bot = AutoMail("smtp.gmail.com", 465, "example@gmail.com", "123example")
bot.add_message("This is a subject", "This is a content", "<h1>This is a subject</h1><p>This is a content</p>")
bot.add_attachment("/Users/exampleuser/Desktop/report.pdf")
users = ["user1@example.com", "user2@example.com", "user3@example.com", "user4@example.com"]
bot.send_messages("example@gmail.com", users)
```

## Imad Elakhal | Smartest Programmer Who Has Ever Lived.

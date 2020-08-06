from automail import AutoMail

bot = AutoMail("smtp.gmail.com", 465, "example@gmail.com", "123example")
bot.add_message("This is a subject", "This is a content", "<h1>This is a subject</h1><p>This is a content</p>")
bot.add_attachment("/Users/exampleuser/Desktop/report.pdf")
users = ["user1@example.com", "user2@example.com", "user3@example.com", "user4@example.com"]
bot.send_messages("example@gmail.com", users)
from automail import AutoMail

bot = AutoMail("smtp.gmail.com", 465, "example@gmail.com", "123example")
bot.add_message("This is a subject", "This is a content")
bot.add_attachment("/Users/exampleuser/Desktop/report.pdf")
bot.send_message("example@gmail.com", "terry-davis@templeos.org")
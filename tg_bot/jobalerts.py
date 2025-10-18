import telebot
import time
import random
import threading

job1 = "https://kwork.ru/projects/2920510"
job2 = "https://kwork.ru/projects/2920498"
job3 = "https://kwork.ru/projects/2920480"
job4 = "https://kwork.ru/projects/2920458"

job_list = [job1, job2, job3, job4]

help = "/help"
start = "/start"
jobs = "/jobs"
notifyme = "/notifyme"

users = {}


bot = telebot.TeleBot("8087355575:AAH9mLVgNN12rgNjchHgukfkixQ040jkiAU")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Hello! \nWelcome to Jobs Alert Bot - your loyal assistant " \
    "that notifies you of the most fresh and interesting jobs on freelance website, Kwork.")

@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(message.chat.id, f"""Welcome to the manual of the commands you can use!
{start} - starts the bot and displays greeting
{help} - displays all the commands to work with
{jobs} - lists a couple of interesting positions available of kwork
{notifyme} - activates notifications of some jobs every minute""")

@bot.message_handler(commands=["jobs"])
def main(message):
    bot.send_message(message.chat.id, f"""<b>Here are some newly published positions:</b>
- <em>One-paged website needed</em>
{job1}
- <em>Teach content processing</em>
{job2}
- <em>Diary app needed</em>
{job3}
- <em>Development of control via mini-app game</em>
{job4}""", parse_mode="html")


@bot.message_handler(commands=["notifyme"])
def main(message):
    user_id = message.from_user.id
    if users.get(user_id):
        bot.send_message(message.chat.id, "You are already signed up for notifications")
        return
    users[user_id] = True
    bot.send_message(message.chat.id, "You have been added to notify-me list. " \
    "You will be updated with new positions every 60 seconds")    
    threading.Thread(target=send_notification, args=(message.from_user.id,), daemon=True).start()
        

@bot.message_handler(commands=["stop"])
def main(message):
    user_id = message.from_user.id
    if users.get(user_id):
        users[user_id] = False
        bot.send_message(message.chat.id, "Notifications disabled")
    else:
        bot.send_message(message.chat.id, "You weren't subscribed for alerts")


def send_notification(user_id):
    while True:
        time.sleep(60)
        if not users.get(user_id, False):
            break
        bot.send_message(user_id, f"""<b>Hey, look at this position!</b> 
Interested? Click the link below 👇
{random.choice(job_list)}""", parse_mode="html")

bot.infinity_polling()

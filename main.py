from os import environ

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import telebot

load_dotenv()

"""
TOKEN is sent by BotFather when you create a telegram bot.
"""
TOKEN = environ.get('TOKEN')

"""
USER_ID is the ID of the telegram user to send the message too. Could be obtained the following way: run the bot in
the polling mode and send something to the bot from the user. The bot needs an event handler.
"""
USER_ID = environ.get('USER_ID')

with open("my_keywords.txt") as fin:
    KEYWORDS = [line.strip() for line in fin]

# Websites from which the news is scrapped
URLS = [
    "https://infomate.club/ml/",
    "https://infomate.club/tech/",
    "https://infomate.club/de/"
]

bot = telebot.TeleBot(TOKEN)


def check_keywords(text):
    lower_text = text.lower()
    for kw in KEYWORDS:
        if kw in lower_text:
            return True
    return False


if __name__ == '__main__':

    for url in URLS:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        for article in soup.find_all(class_="article-link"):
            if check_keywords(article.text) and article.has_attr('href'):
                bot.send_message(
                    USER_ID,
                    f"{article.text} {article['href']}",
                )

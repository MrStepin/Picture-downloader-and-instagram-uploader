import os, instabot
from instabot import Bot 
from dotenv import load_dotenv
load_dotenv()

path_to_dir = "\\Hubble images collection spacecraft"
LOGIN = os.getenv("login")
PASSWORD = os.getenv("password")

list_of_downloaded_images = os.listdir(path_to_dir)
bot = Bot()
bot.login(username = LOGIN, password = PASSWORD)
for image_name in list_of_downloaded_images:
    bot.upload_photo("C:\\Hubble images collection spacecraft\\{}".format(image_name), caption="Autoupload by Py in education purpose only")
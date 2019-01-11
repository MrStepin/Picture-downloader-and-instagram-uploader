import os, instabot
from instabot import Bot 
from dotenv import load_dotenv

PATH_TO_DIR = "\\Hubble images collection spacecraft"

def upload_images_to_instagram(login, password, list_of_downloaded_images):
    bot = Bot()
    bot.login(username = login, password = password)
    for image_name in list_of_downloaded_images:
        bot.upload_photo("C:\\Hubble images collection spacecraft\\{}".format(image_name), caption="Autoupload by Py in education purpose only")

if __name__ == '__main__': 
    load_dotenv()
    login = os.getenv("login")
    password = os.getenv("password")
    list_of_downloaded_images = os.listdir(PATH_TO_DIR)
    upload_images_to_instagram(login, password, list_of_downloaded_images)
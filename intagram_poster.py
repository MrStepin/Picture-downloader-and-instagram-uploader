import os, instabot
from instabot import Bot 
from dotenv import load_dotenv

PATH_TO_DIR = "\\Hubble images collection spacecraft"

def create_list_of_images(PATH_TO_DIR):
    list_of_downloaded_images = os.listdir(PATH_TO_DIR)

def upload_images_to_instagram(LOGIN, PASSWORD, list_of_downloaded_images):
    bot = Bot()
    bot.login(username = LOGIN, password = PASSWORD)
    for image_name in list_of_downloaded_images:
        bot.upload_photo("C:\\Hubble images collection spacecraft\\{}".format(image_name), caption="Autoupload by Py in education purpose only")

if __name__ == '__main__': 
    load_dotenv()
    LOGIN = os.getenv("login")
    PASSWORD = os.getenv("password")
    list_of_downloaded_images = create_list_of_images(PATH_TO_DIR)
    upload_images_to_instagram(LOGIN, PASSWORD, list_of_downloaded_images)
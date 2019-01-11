import requests, os
from os import path

SPACEX_URL = "https://api.spacexdata.com/v3/launches/latest"
PATH_TO_DIR = "\\images"

def download_images(SPACEX_URL):          
    response = requests.get(SPACEX_URL)
    list_of_images = response.json().get("links").get("flickr_images")
    for number, image in enumerate(list_of_images):
        image_response = requests.get(image)
        filename = "image{}.jpg".format(number)
        with open(PATH_TO_DIR+"\\"+filename, 'wb') as picture:  
            picture.write(image_response.content)

if __name__ == '__main__':
    if not os.path.exists(PATH_TO_DIR):
        os.makedirs(PATH_TO_DIR)
    download_images(SPACEX_URL)
import requests, os, instabot
from os import path


COLLECTION = "spacecraft"
HUBBLE_COLLECTION = "http://hubblesite.org/api/v3/images/{}".format(COLLECTION)
PATH_TO_DIR = "\\Hubble images collection {}".format(COLLECTION)

def create_folder(PATH_TO_DIR):
    if not os.path.exists(PATH_TO_DIR):
        os.mkdir(PATH_TO_DIR)

def download_images(HUBBLE_COLLECTION, PATH_TO_DIR):
    response_collection = requests.get(HUBBLE_COLLECTION)
    for image_id in response_collection.json():
        hubble_images = "http://hubblesite.org/api/v3/image/{}".format(image_id.get("id"))
        response = requests.get(hubble_images)
        dict_with_images = response.json().get("image_files")

        list_of_urls = [image_info.get("file_url") for image_info in dict_with_images]
    
        splited_url = list_of_urls[-1].replace(".", "/").split("/")
        response_from_url_to_image = requests.get(list_of_urls[-1])
        filename = "{0}{1}.jpg".format(splited_url[-2], splited_url[-3])

        with open(PATH_TO_DIR+"\\"+filename, 'wb') as picture:  
            picture.write(response_from_url_to_image.content)
        print("Image "+filename+" is downloaded!")

if __name__ == '__main__':
    create_folder(PATH_TO_DIR)
    download_images(HUBBLE_COLLECTION, PATH_TO_DIR)

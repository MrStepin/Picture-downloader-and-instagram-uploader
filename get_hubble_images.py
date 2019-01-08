import requests, os, instabot
from os import path


collection = "spacecraft"
Hubble_collection = "http://hubblesite.org/api/v3/images/{}".format(collection)
path_to_dir = "\\Hubble images collection {}".format(collection)

if not os.path.exists(path_to_dir):
    os.mkdir(path_to_dir)

response_collection = requests.get(Hubble_collection)
for image_id in response_collection.json():
    Hubble_images = "http://hubblesite.org/api/v3/image/{}".format(image_id.get("id"))
    response = requests.get(Hubble_images)
    dict_with_images = response.json().get("image_files")

    list_of_urls = [image_info.get("file_url") for image_info in dict_with_images]
    
    splited_url = list_of_urls[-1].replace(".", "/").split("/")
    response_from_url_to_image = requests.get(list_of_urls[-1])
    filename = "{0}{1}.jpg".format(splited_url[-2], splited_url[-3])

    with open(path_to_dir+"\\"+filename, 'wb') as picture:  
        picture.write(response_from_url_to_image.content)
    print("Image "+filename+" is downloaded!")



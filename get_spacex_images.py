import requests, os
from os import path

spaceX_url = "https://api.spacexdata.com/v3/launches/latest"
path_to_dir = "\\images"

if not os.path.exists(path_to_dir):
    os.mkdir(path_to_dir)
          
response = requests.get(spaceX_url)
list_of_images = response.json().get("links").get("flickr_images")
for number, image in enumerate(list_of_images):
    image_response = requests.get(image)
    filename = "image{}.jpg".format(number)
    with open(path_to_dir+"\\"+filename, 'wb') as picture:  
        picture.write(image_response.content)



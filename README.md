# Space Instagram

These scripts download pictures from spacex and hubble and upload them to instagram  

### How to install

* For using get_spacex_images insert path to folder where you want to download images ```path_to_dir =``` and then execute this in CMD  
* For using get_hubble_images insert colection name to ```collection = ```, and then path to folder where you want to download images ```path_to_dir =``` and then execute this in CMD
* For using instagram_poster create file with name ```.env``` which contain you instagram login and password like this ```login=123``` ```password=111```, path to folder where exist images for uploading ```path_to_dir =``` and then execute this in CMD
Python3 should be already installed.  
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
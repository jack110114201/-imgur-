from imgurpython import ImgurClient
from datetime import datetime
import json
import os

secretFile = json.load(open("secretFile.txt",'r'))

client_id = secretFile['imgur_client_id']
client_secret = secretFile['imgur_client_secret']
access_token = secretFile['imgur_access_token']
refresh_token = secretFile['imgur_refresh_token']
client = ImgurClient(client_id, client_secret, access_token, refresh_token)

def image_upload(image_path,config_album,config_name,config_title,config_description=f'test-{datetime.now()}'):
    config = {
        'album': config_album,
        'name': config_name,
        'title': config_title,
        'description': config_description}
    print("Prepare to uploading image...")
    image_info = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    return image_info

if __name__ == '__main__()':
    image_upload(image_path,config_album,config_name,config_title,config_description=f'test-{datetime.now()}')
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:38:20 2019

@author: Administrator
"""
import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.chdir('C:/Users/Administrator/Desktop/spotify/VisionAPI_demo')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'spotify-transection.json'

client = vision.ImageAnnotatorClient()

def detectText(img):
        
    with io.open(img, 'rb') as image_file:
        content = image_file.read()
        
    image = vision.types.Image(content = content)
    response = client.text_detection(image = image)
    texts = response.text_annotations
    
    df = pd.DataFrame(columns = ['locale','description'])
    for text in texts:
        df = df.append(
                dict(
                    locale = text.locale,
                    description = text.description
                    ),
                    ignore_index = True
                )
    return(df['description'][0])
    

folder_path = r'C:\Users\Administrator\Desktop\spotify\VisionAPI_demo\Images'
song_names = []
for filename in os.listdir(folder_path):
    song_names.append(detectText(os.path.join(folder_path,filename)))

s = ''.join(song_names)
chars = ['回','SQ','Sq','sQ','HQ','vip','VIP','sa','HO','CD','BD','B D',
         '(\n)','SD','GD','@','gO','SO','  D','..']
for c in chars:
    s = s.replace(c,"")

text_file = open("sample.txt", "wt")
n = text_file.write(s.decode('utf-8'))
text_file.close()


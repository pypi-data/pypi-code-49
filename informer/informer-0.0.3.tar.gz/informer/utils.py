# -*- coding: utf-8 -*-
import cv2
import json

def encode_img(img):
    ret, jpeg=cv2.imencode('.jpg', img)
    data = jpeg.tobytes()
    return data

def encode_cmd(v, w, c):
    data = {'v':v, 'w':w, 'c':c}
    data = json.dumps(data).encode()
    return data

def to_json(**kwargs):
    return json.dumps(kwargs)
    
def encode_debug_message(messages):
    data = json.dumps(messages).encode()
    return data
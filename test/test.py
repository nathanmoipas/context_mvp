import requests, json
import pandas as pd

BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE + 'ItemsDB/1')
print(response.text)
#response = requests.get(BASE + "Video/1")
#requests.put(BASE + "Video/1",{"name": "firstvideo","url":"hfbjdbfzvk","duration": 12.0})
#requests.put(BASE + "Video/2",{"name": "secondvideo","url":"bzviuvgiezus","duration": 22.0})
#response = requests.get(BASE + "Video/1")
#print(response.json())
#requests.delete(BASE + "Video/1")
#response = requests.get(BASE + "Video/1")
#print(response.json())

#def a():
 #   return f"nzckubv"
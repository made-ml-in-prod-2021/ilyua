import requests

url = 'http://localhost:80/predict'
myobj = {"f1":0.1,"f2":0.3,"f3":1,"f4":0.9}

x = requests.post(url, data = myobj)

print(x.text)

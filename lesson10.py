#import urllib.request
#opener = urllib.request.build_opener()
#response = opener.open("https://httpbin.org/get")
#print(response.read())
import requests
response = requests.get("https://httpbin.org/get")
print(response.content)
print(f"Datatime - {type(response.content)}")
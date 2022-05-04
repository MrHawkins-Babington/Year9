#yr 9 ISS data lesson

#importing extra Python modules
import json
import urllib.request
import webbrowser

#Accessing Data
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

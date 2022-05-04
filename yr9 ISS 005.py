#yr 9 ISS data lesson
#https://www.geeksforgeeks.org/how-to-track-iss-international-space-station-using-python/

#importing extra Python modules
import json
import urllib.request
import webbrowser

#Accessing Data
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

#create .txt file
file = open("issData.txt", "w")
file.write(
"There are currently " + str(result["number"]) +
" astronauts on the ISS: \n\n")

people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

# load the current status of the ISS in real-time
url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# Extract the ISS location
location = result["iss_position"]
lat = location['latitude']
lon = location['longitude']
#print(lat,lon)

file.write("\nCurrent ISS Latitude: " + str(lat))
file.write("\nCurrent ISS Longitude: " + str(lon))
file.close()
webbrowser.open("issData.txt")

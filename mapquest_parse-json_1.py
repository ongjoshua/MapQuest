import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quezon City, Philippines"
dest = "Pasig City, Philippines"
key = "your_api_key" #Replace with MapQuest Key

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)

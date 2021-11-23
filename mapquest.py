import urllib.parse
import requests
import webbrowser
from operator import length_hint 
from threading import Timer
from flask import *

# Main Program Function

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "fZadaFOY22VIEEemZcBFfxl5vjSXIPpZ"
def configLocation(orig, dest):
    directions = [] 
    roundtripdirections = []
    while True:

        # orig = input("Starting Location: ")
        if orig == "quit" or orig == "q":
            break

        # dest = input("Destination: ")
        if dest == "quit" or dest == "q":
            break

        url = (main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}))
        #print("URL: " + (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            km_calculated = (json_data["route"]["distance"])*1.61
            
            duration = str(json_data["route"]["formattedTime"])
            kilometer  = str("{:.2f}".format(km_calculated)) + " km"
            miles  = str("{:.2f}".format( km_calculated * 0.621371 )) + " miles"
            steps = str("{:.2f}".format( km_calculated * 1312 )) + " steps"
            fuel = str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)) + " ltr"

            for each in json_data["route"]["legs"][0]["maneuvers"]:
                directions.append((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            
            url = (main_api + urllib.parse.urlencode({"key": key, "from":dest, "to":orig}))
            json_data = requests.get(url).json()
            json_status = json_data["info"]["statuscode"]
            roundtrip_km =  (json_data["route"]["distance"])*1.61
            roundtrip =  str("{:.2f}".format(roundtrip_km + km_calculated))  + " km"


            for each in json_data["route"]["legs"][0]["maneuvers"]:
                roundtripdirections.append((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                       
            return [orig, dest, duration, kilometer, roundtrip, steps, fuel, directions, miles, roundtripdirections ]

        elif json_status == 402:
            statusCode = "Status Code: " + str(json_status)
            errorMsg = "Invalid user inputs for one or both locations."
            return [statusCode, errorMsg ]
        elif json_status == 611:
            statusCode = "Status Code: " + str(json_status)
            errorMsg = "Missing an entry for one or both locations."
            return [statusCode, errorMsg ]
        else:
            statusCode ="For Staus Code: " + str(json_status)
            errorMsg =" Refer to: https://developer.mapquest.com/documentation/directions-api/status-codes"
            return [statusCode, errorMsg ]

app = Flask(__name__)

# Load Index html
@app.route('/')
def index():
    return render_template('index.html')
# Getting File Input and Sort & Graph Process
@app.route('/', methods=['POST'])
def upload_files():

    start = request.form['start-location']
    destination = request.form['destination-location']
    result = configLocation(start,destination)
    if length_hint(result) > 2:
        return render_template('result.html', content = result)
    else:
        return render_template('error.html', content = result)


if __name__ == "__main__":
    Timer(1, webbrowser.open_new('http://127.0.0.1:2000/')).start();
    app.run(port=2000)
    app.run(debug=True)
 

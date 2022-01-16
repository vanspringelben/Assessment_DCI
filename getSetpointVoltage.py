import requests
import json
import time

API_URL = "http://188.166.104.86/actions/dcops/device/exercise"
RESULT_FILE = "setpointvoltage.json"
INTERVAL = 5

def fetch():
    response_raw = requests.get(API_URL)
    #print("##### Fetching API")
    return response_raw.json()


def getSetpointVoltage(input):
    voltage = input["elements"]["7d520da4-3283-45bf-98c2-02b371e63a4a"]["control"]["ports"]["top"]["voltage"]
    return int(voltage)

def saveResult(voltage):
    output = {"setpointVoltage": voltage}
    with open(RESULT_FILE, 'w') as outfile:
        #print("##### Saving JSON")
        json.dump(output, outfile)

def main():
    while(True):
        API_result = fetch()
        setpointVoltage = getSetpointVoltage(API_result)
        saveResult(setpointVoltage)
        time.sleep(INTERVAL)

main()
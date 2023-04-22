print("--------------------------------------------------------------------------------------------------")

print("Ping hosts using the requests and os libraries to perform HTTP requests and manage system functions.")
import os

urls = ['dashboard.tradingblock.com',
       'api3.tradingblock.com','dashboardapi.tradingblock.com','ws.tradingblock.com',
       'vt.tradingblock.com',
       'application.tradingblock.com','tradingblock.com']
for url in urls:
    # Use ping to check the availability of the URL
    response = os.system("ping -c 1 " + url)

    # Check the response code whether URL is available or not
    if response == 0:
        print(url + " is running.")
    else:
        print(url + " is not running.")


print("--------------------------------------------------------------------------------------------------")

print("--------------------------------------------------------------------------------------------------")

print("Verify the validity of the GetRequirements RestHub endpoint:")

dict_Datatype= {
  "dict1": {
    "minLength": int,
    "maxLength": int,
    "minDigitCount": int,
    "minSpecialCount": int,
    "acceptableSpecialChars": str
  },
  "dict2": {
    "minCharAllowed": str,
    "maxCharAllowed": str,
    "minLowerCount": int,
    "minUpperCount": int,
    "minDigitCount": int,
    "minSpecialCount": int,
    "minLength": int,
    "maxLength": int,
    "preferredMinLength": int
  }
}

payload = {
    "nameRequirements": {
      "minLength": 6,
      "maxLength": 30,
      "minDigitCount": 0,
      "minSpecialCount": 0,
      "acceptableSpecialChars": "~!#$=+._"
    },
    "passwordRequirements": {
      "minCharAllowed": "!",
      "maxCharAllowed": "~",
      "minLowerCount": 1,
      "minUpperCount": 1,
      "minDigitCount": 1,
      "minSpecialCount": 1,
      "minLength": 8,
      "maxLength": 0,
      "preferredMinLength": 12
    }
  }

for key in dict_Datatype["dict1"]:
    value = payload["nameRequirements"].get(key)
    data_type = dict_Datatype["dict1"].get(key)
    if isinstance(value, data_type):
        print(f"{key}: {value} is of type {data_type}")
    else:
        print(f"{key}: {value} is not of type {data_type}")

for key in dict_Datatype["dict2"]:
    value = payload["passwordRequirements"].get(key)
    data_type = dict_Datatype["dict2"].get(key)
    if isinstance(value, data_type):
        print(f"{key}: {value} is of type {data_type}")
    else:
        print(f"{key}: {value} is not of type {data_type}")


print("--------------------------------------------------------------------------------------------------")

print("--------------------------------------------------------------------------------------------------")

print("Bonus: Implement a continuous monitoring feature that pings the endpoints every 1 minute.")
import time
import requests

hosts = ['dashboard.tradingblock.com',
       'api3.tradingblock.com','dashboardapi.tradingblock.com','ws.tradingblock.com',
       'vt.tradingblock.com',
       'application.tradingblock.com','tradingblock.com']

#loop for continuous monitoring
while True:
    print(f"Monitoring started at {time.strftime('%H:%M:%S on %m-%d-%Y')}")

    for host in hosts:
        try:
            response = requests.get(host)
            if response.status_code == 200:
                print(f"{host} is up!")
            else:
                print(f"{host} returned status code {response.status_code}")
        except requests.exceptions.RequestException as error:
            print(f"{host} is down: {error}")

    # It will wait for one minute before run again
    time.sleep(60)
    


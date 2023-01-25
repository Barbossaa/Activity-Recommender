import requests
import json

print("You seem bored but don't worry this is why i am here. Here is the list of what types of activities you can deal. ")
print("-education")
print("-recreational")
print("-social")
print("-diy")
print("-charity")
print("-relaxation")
print("-music")
print("-busywork")

type = input("What do you enjoy most from above? : ")

# pa_num = input("How many person are you looking an activity with? (If just you, type 1.)")

api_url = "http://www.boredapi.com/api/activity?type={}".format(type)

response = requests.get(api_url)
activity = json.loads(response.text)["activity"]

print("Activity : " + activity)
print("Reference : Bored API")

input("Press enter to proceed...")

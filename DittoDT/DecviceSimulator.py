import requests
import time


url = "http://localhost:8080/api/2/things"
login = ('ditto', 'ditto')
thingId = ""


with open("thingId.txt", "r") as file:
    thingId = file.readline()

print("Successfully read thingId:", thingId)

max_charge = float(requests.get((url+"/"+thingId+"/features/electricity/properties/max_capacity"), auth = login).text)

def update_data():
    # getting consumption, charge from DT to match with engines consumption
    # in a real example the twin and the real consumption could be compared at this point
    # the charge level would be read from internal sensors
    consumption = float(requests.get((url+"/"+thingId+"/features/electricity/properties/consumption"), auth = login).text)
    charge = float(requests.get((url+"/"+thingId+"/features/electricity/properties/charge"), auth = login).text)

    charge -= consumption+50 #TODO remove if connected
    print("new charge level:", charge)

    if (charge/max_charge < 0.1):
        # throwing events
        print("battery low!")

    response = requests.put((url+"/"+thingId+"/features/electricity/properties/charge"), data = str(charge), auth = login)

while True:
    update_data()
    time.sleep(5)

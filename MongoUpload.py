import datetime
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1 #makes voltage readable, no multiplier necessary
adc.start_adc(0, gain=GAIN) #converts analog to digital

client = MongoClient()
db = client.embrace

#poll the sensor
while (true):
    #load = adc.get_last_result()
    load = 5
    date = timeline.timeline.utcnow

    datum = {
        "date": date,
        "load": load
    }

    db.embrace.insert_one(
        datum
    )

    time.sleep(1)

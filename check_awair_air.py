#!/usr/bin/env python3
import requests
import json

# the DNS hostname or IP addresss of your Awaire with Local Sensors enabled
hostname = 'AWAIR-R2-1313EC.local.'

u = 'http://' + hostname + '/air-data/latest'
r = requests.get(u)
if r.status_code != 200:
    print(f"Unable to reach sensor at {u}")
    exit(1)
d = r.json()

out = """Air Quality:
Score:      {:5.0f}
Temp:       {:5.0f}
Humidity:   {:5.0f}
CO2:        {:5.0f}
Chemicals:  {:5.0f}
PM2.5:      {:5.0f}
""".format(d['score'], 
           d['temp'],
           d['humid'],
           d['co2'],
           d['voc'],
           d['pm25'])

print(out)

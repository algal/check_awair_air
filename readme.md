# Awair CLI

This "project" is just two Python scripts for checking the air quality
sensed by your Awair sensors from the command line.

## How to use

This is dirt simple. It doesn't rely on OAUTH or any servers. It
relies on enabling "Local Sensors" on your Await

- `check_awair_air.py` queries your device and reports scores. You need to
  edit this file so the variable `hostname` hass the hostname or IP
  addresss of your device on your local network. You can find this
  information by checking your router or ...

- `find_awair_url.py` can help you find this information. It reports
  the IP address and the mDNS hostname. The advantage of using an mDNS
  hostname instead of an IP address is you don't have to worry about
  it changing. You will need to `pip install zeroconf` for
  `find_awair_url.py` to work.

To enable Local Sensors on your Awair, open the Awair app, go to your
device, Settings, Developer Options, Enable Local Sensors.


Output looks like this:


```
❯ ./check_air.py 
Air Quality:
Score:         77
Temp:          25
Humidity:      57
CO2:          738
Chemicals:    367
PM2.5:         39
```

The API actually reports more data, which you can get at easily by exploring the JSON.

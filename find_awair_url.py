#!/usr/bin/env python3
# requirements: Python 3.5+
# requirements: pip install zeroconf
import socket
from zeroconf import ServiceBrowser, Zeroconf
from typing import cast
import time

# time in seconds to search for an Awair with "Local Sensors" enabled
# we assume any service with the name starting with "awair" and
# advertising an HTTP server is a device
time_to_search = 5 # (seconds)


def is_awair(name):
    for prefix in ['AWAIR-R2-','ELEM-','OMNI-','MNT-']:
        if name.startswith(prefix):
            return True
    return False

# finds the mDNS hostname and the IP address of the first Awair sensor found on your network
class FirstAwairListener:
    def __init__(self):
        self.ip_url = None
        self.name_url = None
    
    def remove_service(self, zeroconf, type, name):
        pass

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if is_awair(name) and info.type == '_http._tcp.local.':
            addresses = ["%s:%d" % (socket.inet_ntoa(addr), cast(int, info.port)) for addr in info.addresses]
            self.ip_url = "http://" + addresses[0]
            self.name_url = "http://" + info.server

# untested! I've only got one device, yo.
class AllAwairListener:
    def __init__(self):
        self.inet_urls = []
        self.name_urls = []
    
    def remove_service(self, zeroconf, type, name):
        pass

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if is_awair(name) and info.type == '_http._tcp.local.':
            inet_url = ["http://%s:%d" % (socket.inet_ntoa(addr), cast(int, info.port)) for addr in info.addresses][0]
            hostname_url = "http://" + info.server
            self.inet_urls.append(inet_url)
            self.name_urls.append(hostname_url)

zeroconf = Zeroconf()
listener = FirstAwairListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)

time.sleep(time_to_search)
if listener.name_url is None:
    print(f"No Awair devices found in {time_to_search} seconds")
else:
    print(f"{listener.name_url}\t->\t{listener.ip_url}")

zeroconf.close()

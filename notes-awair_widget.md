# Awair

## 2020-10-01T1051 


## Posssible resources

URL for latest data reading: http://192.168.4.43/air-data/latest

annotated data sample:

```json
{"timestamp":"2020-10-01T17:49:19.760Z",
 "score":76,         # score
 "dew_point":15.76,
 "temp":24.02,
 "humid":59.96,      # humid
 "abs_humid":13.03,
 "co2":1089,         # co2
 "co2_est":1437,
 "voc":520,          # voc
 "voc_baseline":2363789784,
 "voc_h2_raw":24,
 "voc_ethanol_raw":34,
 "pm25":23,          #PM2.5
 "pm10_est":24}
```


## Awair sensor zeroconf servie data:

Advertises itself.

Service Name: AWAIR-R2-1313EC
Service Type: WWW HTTP
DNS-SD Name: `_http._tcp`
Host: AWAIR-R2-1313EC.local.
Service address: 192.168.4.43
Port: 80
Txt Data: None







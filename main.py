from pythonping import ping
import requests
import subprocess
import time
response_list=ping('155.133.232.98')
print("==FireLat v1.0== \nSimple utility to fix ISP routing issues.")
lat=response_list.rtt_avg_ms
print("IP before run-time: ",requests.get("http://ipconfig.in/ip").text)
print("Latency before run-time= ",lat,"ms")
while lat>49:
    print("Restarting Modem..")
    subprocess.run('restart.exe')
    time.sleep(63)
    print("Restart Complete.")
    response_list=ping('155.133.232.98')
    ip=getip.get()
    lat=response_list.rtt_avg_ms
    if lat<49:
        break
print("Current latency= ",lat,"ms")
print("IP address: ",requests.get("http://ipconfig.in/ip").text)
input("Press Enter to Quit.")
    

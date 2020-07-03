from pythonping import ping
import subprocess
import time
response_list=ping('155.133.232.98')
print("==FireLat v1.0== \nSimple utility to fix ISP routing issues.")
lat=response_list.rtt_avg_ms
print("Current Ping= ",lat,"ms")
while lat>45:
    print("Restarting Modem..")
    subprocess.run('restart.exe')
    time.sleep(63)
    print("Restart Complete.")
    response_list=ping('155.133.232.98')
    lat=response_list.rtt_avg_ms
    if lat<45:
        break
print("Current latency= ",lat,"ms")
input("Press Enter to Quit.")
    

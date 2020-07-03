from pythonping import ping
import subprocess
import time
response_list=ping('155.133.232.98')
print("==FireLat v1.0== \nSimple utlity to fix ISP routing issues.")
print("Current Ping= ",response_list.rtt_avg_ms)
while response_list.rtt_avg_ms>39:
    print("Restarting Modem..")
    subprocess.run('restart.exe')
    time.sleep(63)
    print("Restart Complete.")
    response_list=ping('155.133.232.98')
    if response_list.rtt_avg_ms>39:
        print("Current latency= ",response_list.rtt_avg_ms)
        break
    else:
        continue
print("Current latency= ",response_list.rtt_avg_ms)
    
    

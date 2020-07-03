from pythonping import ping
response_list=ping('155.133.232.98')
print("==FireLat v1.0== \nSimple utlity to fix ISP routing issues \nFixing routes..")
print("Current Ping= ",response_list.rtt_avg_ms)



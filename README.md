# FireLat
Simple Utility to check ping to a server and restart the router/modem if the ping is bad or above your desired range automatically until you get better ping. I made this for my personal use, As my ISP uses different routing for each of their IP ranges. What this program does is check the latency to the given server and then restarts the modem until a better latency is acheived. It works based on Telnet(Restarting the modem), and the script can be custom tuned to work with your modem. The Python script can be also fine tuned to suit your need, like setting custom server IPs as target server IP(Default server IP is Valve South India Server). 

For running the firelat.py you need to have Python 3.7 and some modules installed. 

To install those modules, Simply run these commands in your CMD.

pip install requests

pip install pythonping

After running these commands, Run firelat.py to start the program. 

 

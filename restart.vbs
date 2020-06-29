Option explicit
Dim oShell
set oShell= Wscript.CreateObject("WScript.Shell")
oShell.Run "telnet"
WScript.Sleep 1000
oShell.Sendkeys "open 192.168.1.1~"
WScript.Sleep 1000
oShell.Sendkeys "admin~"
WScript.Sleep 1000
oShell.Sendkeys "messb0i5trange~"
WScript.Sleep 1000
oShell.Sendkeys "reboot~"
WScript.Sleep 3000
oShell.Sendkeys "exit~"
WScript.Sleep 3000
oShell.Sendkeys "t~"
WScript.Sleep 3000
oShell.Sendkeys "q~"

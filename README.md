# uptime_monitor
Simple Python 3 script that monitors network uptime only using standard libraries

Currently set up to just call urllib.request.urlopen on https://www.google.com every 20 seconds
and log if it connected, or any errors it had when trying to connect, along with the timestamp

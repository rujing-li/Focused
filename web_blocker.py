from datetime import datetime as dt
import time

unix_hosts_path = "/etc/hosts"
win_hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# the os that user is on
hosts_path = unix_hosts_path
# list of websites to block
block_list = ["www.youtube.com", "www.netflix.com", "youtube.com", "netflix.com"]
# starting and ending time of the focusing period
start_hour = 0
start_min = 0
end_hour = 22
end_min = 59

while True:
  if dt (dt.now ().year, dt.now ().month, dt.now ().day, start_hour, start_min) < dt.now () < dt (dt.now ().year, dt.now ().month, dt.now ().day, end_hour, end_min):
    print ("Focus time, blocking websites selected.")
    with open (hosts_path, 'r+') as file:
      content = file.read ()
      for site in block_list:
        if site in content:
          pass
        else:
          file.write(redirect + " " + site + "\n")
  else:
    with open (hosts_path, 'r+') as file:
      lines = file.readlines ()
      file.seek (0)
      for line in lines:
        if not any (site in line for site in block_list):
          file.write(line)
      file.truncate ()
    print ("Time to relax! No websites blocked.")
  time.sleep(5)
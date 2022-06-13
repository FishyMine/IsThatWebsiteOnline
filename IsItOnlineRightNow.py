# View the github here: https://github.com/FishyMine/IsThatWebsiteOnline
# Fully made by FishyMine
try: 
  import time 
  print("######## Is it online right now? v1.0.1 ########")
  time.sleep(0.9)
  print("Want more? Add more stuff to this project! https://github.com/FishyMine/IsThatWebsiteOnline")
  time.sleep(0.9)
  print("Please wait while the console installs all of the packages.")
  import urllib.request
  import socket
  print("Please enter the website URL -- NO SPACES, NUMBERS, OR SYMBOLS (URL MUST BE VALID)")
  print("DONT ADD HTTPS:// OR HTTP://")
  website = input()
  print ("-------------------------PLEASE WAIT---------------------------")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
   
except:
    print("This website is not available, suspended, or doesnt exist.")
    exit(0)
if result == 0:
    
   print ("Website is currently online and detected")
else:
   print ("Website is offline or not detected")

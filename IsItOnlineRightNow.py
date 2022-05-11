import time 
print("######## Is it online right now? ########")
time.sleep(0.9)
print("Please wait while the console installs all of the packages.")
import urllib.request
import socket
time.sleep(2)
print("Please enter the website URL -- NO SPACES, NUMBERS, OR SYMBOLS (URL MUST BE VALID)")
website = input()
print ("-------------------------PLEASE WAIT---------------------------")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((website, 80))
try: 

   
   time.sleep(2)
except:
    print("This website is not available, suspended, or doesnt exist.")
      waitend = input()

if result == 0:
    
   print ("Website is currently online and detected")
   waitend = input()
else:
   print ("Website is offline or not detected")
   waitend = input()

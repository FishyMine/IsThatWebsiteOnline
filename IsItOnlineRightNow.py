# View the github here: https://github.com/FishyMine/IsThatWebsiteOnline
# Fully made by FishyMine

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
try: 
  import time 
  print(bcolors.OKBLUE + "######## Is it online right now? v1.0.1 ########")
  time.sleep(0.9)
  print("Want more? Add more stuff to this project! https://github.com/FishyMine/IsThatWebsiteOnline")
  time.sleep(0.9)
  print(bcolors.WARNING + "Please wait while the console installs all of the packages.")
  import urllib.request
  import socket
  import json
  print(bcolors.BOLD + "Please enter the website URL -- NO SPACES, NUMBERS, OR SYMBOLS (URL MUST BE VALID)")
  print("DONT ADD HTTPS:// OR HTTP://")
  
  
  website = input()
  print (bcolors.HEADER + "-------------------------PLEASE WAIT---------------------------")
  print(bcolors.OKBLUE + "Checking...")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "10%")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "20%")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "30%")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "40%")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "50%")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "60%")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "70%")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "80%")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "90%")
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((website, 80))
  print(bcolors.OKBLUE + "100%")
except:
    print(bcolors.FAIL + "This website is not available, suspended, or doesnt exist.")
    exit()
if result == 0:
    
   print (bcolors.OKGREEN + "Website is currently online and detected")
else:
   print (bcolors.FAIL + "Website is offline or not detected")

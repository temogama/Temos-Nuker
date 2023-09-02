##########thelinuxuxer-choice#################
#############subodha prabash ##########
###########ip tracker v 1 ######
# importing the necessary packages 
import time 
import sys 
import os 
  
# Function for implementing the loading animation 
def load_animation(): 
  
    # String to be displayed when the application is loading 
    load_str = "Loading..."
    ls_len = len(load_str) 
  
  
    # String for creating the rotating line 
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of 
    # the duration of animation 
    counttime = 0        
      
    # pointer for travelling the loading string 
    i = 0                     
  
    while (counttime != 30): 
          
        # used to change the animation speed 
        # smaller the value, faster will be the animation 
        time.sleep(0.075)  
                              
        # converting the string to list 
        # as string is immutable 
        load_str_list = list(load_str)  
          
        # x->obtaining the ASCII code 
        x = ord(load_str_list[i]) 
          
        # y->for storing altered ASCII code 
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered 
        # switch uppercase to lowercase and vice-versa  
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        # for storing the resultant string 
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        # displaying the resultant string 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        # Assigning loading string 
        # to the resultant string 
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
    # for windows OS 
    if os.name =="nt": 
        os.system("cls") 
          
    # for linux / Mac OS 
    else: 
        os.system("clear") 
  
# Driver program 
if __name__ == '__main__':  
    load_animation() 
#####end loding######
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
############banner

banner = r'''
  _____         _______             _             
 |_   _|       |__   __|           | |            
   | |  _ __      | |_ __ __ _  ___| | _____ _ __ 
   | | | '_ \     | | '__/ _` |/ __| |/ / _ \ '__|
  _| |_| |_) |    | | | | (_| | (__|   <  __/ |   
 |_____| .__/     |_|_|  \__,_|\___|_|\_\___|_|   
       | |                                        
       |_|                                        

'''



prCyan(banner)

#######types

from time import sleep
import sys
print("█████████████████████████████████████")
line_1 = "███Temo`s Multitool - Ip Tracker ████ "
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)

print("\n█████████████████████████████████████")
import sys
import os
################colors######
WARNING = '\033[93m' #nothing
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 



prGreen(" [1] - Get your ip address information  ")
prGreen(" [2] - Get ip address information   ")
prGreen(" Type 'exit' to go back in main menu  ")
option = input(''' ┌─[ Temo`s Multitool ]─[~]
 └──╼ # ''')




##############
while True:
  if option == "1":
################
      from requests import get
      myip = get('https://ipapi.co/json/')
      prYellow(myip.json())
      import sys
      sys.exit()
      
                
  elif option == "2" :
###############
      from requests import get
      ip = input("Enter your ip:")
      track = get(f'https://ipapi.co/{ip}/json/')
      prYellow(track.json())
      import sys
      sys.exit()
  else:
##############
      prRed("closing....")
      prRed("thank you for using tool!")
      import sys
      sys.exit()
      
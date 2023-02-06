import os
from pyautogui import write, press
from time import sleep 

#make sure to instal pyautogui by running the below command on the terminal
#pip install pyautogui 
#sleep arguments might need some changes
def x():
    press("enter")

os.startfile(r"") #paste file location of command prompt. don't remove the 'r'.
sleep(1)
write("ssh @gatekeeper.cs.hku.hk") #enter cs account
x()
sleep(1)
write("") #enter password
x()
write("ssh @academy.cs.hku.hk") #enter cs account
x()
sleep(2)
write("") #enter password
x()

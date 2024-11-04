import os
from pyautogui import write, press
from time import sleep 

def x():
    press("enter")

os.startfile(r"") # enter filepath to command prompt
sleep(1)
pw = "<password>"
write("ssh <user_name>@gatekeeper.cs.hku.hk")
x()
sleep(1)
write(pw)
x()
write("ssh <user_name>@i7.cs.hku.hk")
x()
sleep(1)
write(pw)
x()
sleep(2)
write("cd public_html")
x()
sleep(1)
write("mysql -h sophia -u <user_name> -p")
x()
sleep(1)
write(pw[:8])
x()

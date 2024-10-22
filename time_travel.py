import sys
import datetime

import pyautogui
import time

def _linux_set_time(time_tuple): 
    import subprocess 
    import shlex 
 
    time_string = time_tuple.isoformat()

    print(f'Setting system time to {time_string}')
 
    #subprocess.call(shlex.split("timedatectl set-ntp false")) # may be necessary 
    subprocess.call(shlex.split("sudo date -s '%s'" % time_string)) 
    subprocess.call(shlex.split("sudo hwclock -w")) 
 

def move_mouse_get_money():
    
    # move mouse to browser button
    pyautogui.moveTo(663, 776, duration=1)

    # click browser button
    pyautogui.click()

    # wait for browser to load
    time.sleep(2)

    # type URL and press enter
    pyautogui.typewrite('https://www.youtube.com/playables/Ugkxl5VAVrIKHF5GRmanrMwq2VtumP3V6uOw\n', interval=.25)

    # wait for website to load
    #time.sleep(6)

    # move mouse to stateio thumbnail
    #pyautogui.moveTo(246, 503, duration=1)

    # click stateio thumbnail
    #pyautogui.click()

    # wait for game to load
    time.sleep(10)

    # move mouse to continue button
    pyautogui.moveTo(644, 594, duration=1)

    # click continue button
    pyautogui.click()

    # move mouse to close window button
    pyautogui.moveTo(1269, 54, duration=1)

    # wait a sec
    time.sleep(1)

    # click close window button
    pyautogui.click()

    # move mouse to leave page button
    pyautogui.moveTo(795, 503, duration=1)

    # wait a sec
    time.sleep(1)

    # click leave page button
    pyautogui.click()
	
# start and stop times are based on when the security certificate is valid
start_datetime = datetime.datetime(2024, 10, 22)
end_datetime = datetime.datetime(2025, 1, 12)

_linux_set_time(start_datetime)

while True:
    system_time_human = datetime.datetime.now().isoformat()
    print(f'Current system time: {system_time_human}')
    time.sleep(2)
    move_mouse_get_money()
    
    # increment 12 hours
    current_datetime = datetime.datetime.now()
    new_datetime = current_datetime + datetime.timedelta(hours=12)
    _linux_set_time(new_datetime)

    if new_datetime >= end_datetime:
        _linux_set_time(start_datetime)

print("Reached end datetime!", current_datetime)

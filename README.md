# YouTube Playable Automation Script

This Python script automates interactions with a specific YouTube playable game, adjusting the system time to repeatedly play the game.

## Description

This script performs the following actions:
1. Sets the system time to a specific start date
2. Opens a web browser and navigates to a specific YouTube playable game
3. Interacts with the game using mouse movements and clicks
4. Closes the browser window
5. Increments the system time by 12 hours
6. Repeats the process until reaching an end date, then resets to the start date

## Dependencies

This script requires the following Python libraries:
- sys
- datetime
- pyautogui
- time

Install the required libraries using pip:

pip install pyautogui


## Usage

Run the script with Python 3:

python3 time_travel.py


Note: This script requires sudo privileges to modify the system time on Linux systems.

## Important Notes

- This script is designed for a specific YouTube playable game and uses hardcoded screen coordinates for mouse movements. It may not work correctly on different screen resolutions or setups.
- Modifying system time can have unintended consequences. Use with caution. Or a VM.
- The script runs indefinitely until manually stopped.

## Disclaimer

This script is for educational purposes only. Be aware that automating interactions with web services may violate te terms of service. Use responsibly and at your own risk.


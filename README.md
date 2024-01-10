# Programmable-Auto-Keyboard-Presser
Python Script to simulate keyboard key presses using pynput but you can set a sequence of commands with the buttons to press and the delay times. This works in FiveM!!

### Requirements:
- Python
- pynput

# Installing pynput
1. Open your cmd/terminal.
1. type ```pip install pyautogui``` and press enter.
1. after installation close the console.


# How to use
1. You need to start the `core.py` with python.
2. You need to write a `prompt`, the prompt is the sequence of commands. E.g.`e,2,r,4,enter,1.5,caps_lock,0.5,t,1`
   ### Prompt Syntax:
   > The input prompt must be have this format: {button_name},{delay_time_in_sec},{button_name},{delay_time_in_sec}
3. After prompt you have to enter how many times you want the prompt to be executed. (if you enter -1 it will execute the prompt until you close it.)

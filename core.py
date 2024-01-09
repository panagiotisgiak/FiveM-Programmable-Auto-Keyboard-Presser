from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

queue = []
temp = 1

specialbutton = {
    "alt":Key.alt,
    "alt_l":Key.alt_l,
    "alt_r":Key.alt_r,
    "backspace":Key.backspace,
    "caps_lock":Key.caps_lock,
    "cmd":Key.cmd,
    "cmd_l":Key.cmd_l,
    "cmd_r":Key.cmd_r,
    "ctrl":Key.ctrl,
    "ctrl_l":Key.ctrl_l,
    "ctrl_r":Key.ctrl_r,
    "delete":Key.delete,
    "down":Key.down,
    "end":Key.end,
    "enter":Key.enter,
    "esc":Key.esc,
    "f1":Key.f1,
    "f2":Key.f2,
    "f3":Key.f3,
    "f4":Key.f4,
    "f5":Key.f5,
    "f6":Key.f6,
    "f7":Key.f7,
    "f8":Key.f8,
    "f9":Key.f9,
    "f10":Key.f10,
    "f11":Key.f11,
    "f12":Key.f12,
    "home":Key.home,
    "insert":Key.insert,
    "left":Key.left,
    "menu":Key.menu,
    "num_lock":Key.num_lock,
    "page_down":Key.page_down,
    "page_up":Key.page_up,
    "pause":Key.pause,
    "print_screen":Key.print_screen,
    "right":Key.right,
    "scroll_lock":Key.scroll_lock,
    "shift":Key.shift,
    "shift_l":Key.shift_l,
    "shift_r":Key.shift_r,
    "space":Key.space,
    "tab":Key.tab,
    "up":Key.up
}

queue = input('Write prompt: ')
queue = queue.split(",")

times = int(input('how many times you want it to repeat (-1 for unlimited): '))
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

if times == -1:#unlimited
    while True:
        for i in range(0, len(queue)):
            if((i+1) % 2 != 0):
                if (queue[i] in specialbutton):
                    keyboard.press(specialbutton[queue[i]])
                    time.sleep(0.1)
                    keyboard.release(specialbutton[queue[i]])
                    time.sleep(0.1)
                else:
                    keyboard.press(queue[i])
                    time.sleep(0.1)
                    keyboard.release(queue[i])
                    time.sleep(0.1)
            else:
                print(queue[i]," delay")
                time.sleep(int(queue[i]))
else:#limited
    while temp <= times:
        temp += 1
        for i in range(0, len(queue)):
            if((i+1) % 2 != 0):
                if (queue[i] in specialbutton):
                    keyboard.press(specialbutton[queue[i]])
                    time.sleep(0.1)
                    keyboard.release(specialbutton[queue[i]])
                    time.sleep(0.1)
                else:
                    keyboard.press(queue[i])
                    time.sleep(0.1)
                    keyboard.release(queue[i])
                    time.sleep(0.1)
            else:
                time.sleep(int(queue[i]))